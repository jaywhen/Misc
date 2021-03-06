from thegram import app
from flask import render_template, url_for, redirect, request, flash, get_flashed_messages, send_from_directory
from thegram.models import User, Image, db, Comment
from flask_login import login_user, logout_user, current_user, login_required
from qiniusdk import qiniu_upload_file
import random, hashlib, json, uuid, os


# 将用户上传的图片直接保存到服务器
def save_to_local(file, file_name):
   save_dir = app.config['UPLOAD_DIR']
   file.save(os.path.join(save_dir, file_name))
   return '/image/' + file_name

# 将用户上传的图片保存到七牛云
def save_to_qiniu(file, filename):
   return qiniu_upload_file(file, filename)


@app.route('/image/<image_name>')
def view_image(image_name):
   return send_from_directory(app.config['UPLOAD_DIR'], image_name)

def redirect_with_msg(target, msg, category):
   if msg != None:
      flash(msg, category = category)
   return redirect(target)

@app.route('/')
def index():
   images = Image.query.order_by(Image.id.desc()).limit(10).all()
   return render_template('index.html', images = images)

@app.route('/image/<int:image_id>')
def image(image_id):
   image = Image.query.get(image_id)
   if image == None:
      # 跳转首页测试用，后期写跳转页
      return redirect('/')
   return render_template('pageDetail.html', image = image)

@app.route('/profile/<int:user_id>')
@login_required
def profile(user_id):
   user = User.query.get(user_id)
   if user == None:
      return redirect('/')
   paginate = Image.query.filter_by(user_id = user_id).paginate(page=1, per_page=3, error_out=False)
   return render_template('profile.html', user = user, images = paginate.items, has_next = paginate.has_next)

@app.route('/profile/images/<int:user_id>/<int:page>/<int:per_page>/')
def user_images(user_id, page, per_page):
   paginate = Image.query.filter_by(user_id = user_id).paginate(page=page, per_page=per_page, error_out=False)
   map = {'has_next': paginate.has_next}
   images = []
   for image in paginate.items:
      imgvo = {
         'id':image.id,
         'url':image.url, 
         'comment_count':len(image.comments)
         }
      images.append(imgvo)
   map['images'] = images
   return json.dumps(map)

@app.route('/regloginpage')
def regloginpage():
   msg = ''
   for m in get_flashed_messages(with_categories=False, category_filter=['reglogin']):
      msg = msg + m
   return render_template('login.html', msg = msg, next = request.values.get('next'))

@app.route('/reg', methods = ['GET', 'POST'])
def reg():
   username = request.values.get('username').strip()
   password = request.values.get('password').strip()

   user = User.query.filter_by(username = username).first()
   if username == '' or password == '':
      return redirect_with_msg(url_for('regloginpage'), '用户名或密码为空！', 'reglogin')

   if user != None:
      return redirect_with_msg(url_for('regloginpage'), '用户名已存在👌', 'reglogin')

   # 将新用户入表
   salt = '.'.join(random.sample('0123456789abcdefgABCDEFG', 10))
   m = hashlib.md5()
   m.update(password.encode('utf-8') + salt.encode('utf-8'))
   password = m.hexdigest()
   user = User(username, password, salt)
   db.session.add(user)
   db.session.commit()

   login_user(user)

   next = request.values.get('next')
   if next != None and next.startswith('/') > 0:
      return redirect(next)

   return redirect('/')

@app.route('/login', methods = ['GET', 'POST'])
def login():
   username = request.values.get('username').strip()
   password = request.values.get('password').strip()

   
   if username == '' or password == '':
      return redirect_with_msg(url_for('regloginpage'), '用户名或密码为空！', 'reglogin')

   user = User.query.filter_by(username = username).first()

   if user == None:
      return redirect_with_msg(url_for('regloginpage'), '用户名不存在！', 'reglogin')

   m = hashlib.md5()
   m.update(password.encode('utf-8') + user.salt.encode('utf-8'))
   if (m.hexdigest() != user.password):
      return redirect_with_msg(url_for('regloginpage'), '密码不正确！', 'reglogin')

   login_user(user)

   next = request.values.get('next')
   if next != None and next.startswith('/'):
      return redirect(next)

   return redirect('/')
   
@app.route('/logout')
def logout():
   logout_user()
   return redirect('/')
   
@app.route('/upload', methods = ['POST'])
def upload():
   file = request.files["file"]
   file_ext = ''
   if file.filename.find('.') > 0:
      file_ext = file.filename.rsplit('.', 1)[1].strip().lower()
   if file_ext in app.config['ALLOWED_EXT']:
      file_name = str(uuid.uuid1()).replace('-', '') + '.' + file_ext
      # url = save_to_local(file, file_name)
      url = save_to_qiniu(file, file_name)
      if url != None:
         upload_img = Image(url, current_user.id)
         db.session.add(upload_img)
         db.session.commit()
   
   return redirect('/profile/%d' % current_user.id)

@app.route('/addcomment/', methods = ['POST'])
@login_required
def add_comment():
   image_id = int(request.values['image_id'])
   content = request.values['content']
   comment = Comment(content, image_id, current_user.id)
   
   
   db.session.add(comment)
   db.session.commit()

   return json.dumps({
      "code":0,
      "id":comment.id,
      "content":comment.content,
      "username":comment.user.username,
      "user_id":comment.user_id
   })

   

@app.route('/legal/terms')
def legal_terms():
   pass

@app.route('/legal/privacy')
def legal_privacy():
   pass