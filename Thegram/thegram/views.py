from thegram import app

from flask import render_template, url_for, redirect, request, flash, get_flashed_messages
from thegram.models import User, Image, db
import random, hashlib



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
def profile(user_id):
   user = User.query.get(user_id)
   if user == None:
      return redirect('/')
   return render_template('profile.html', user = user)

@app.route('/regloginpage')
def regloginpage():
   msg = ''
   for m in get_flashed_messages(with_categories=False, category_filter=['relogin']):
      msg = msg + m
   return render_template('login.html', msg = msg)

@app.route('/login', methods = ['GET', 'POST'])
def login():
   username = request.values.get('username').strip()
   password = request.values.get('password').strip()

   user = User.query.filter_by(username = username).first()
   if username == '' or password == '':
      return redirect_with_msg(url_for('regloginpage'), '用户名或密码为空！', 'relogin')

   if user == None:
      return redirect_with_msg(url_for('regloginpage'), '用户名不存在！', 'relogin')

   m = hashlib.md5()
   m.update(password.encode('utf-8') + user.salt.encode('utf-8'))
   if (m.hexdigest() != user.password):
      return redirect_with_msg(url_for('regloginpage'), '密码不正确', 'reglogin')

   return redirect('/')




@app.route('/reg', methods = ['GET', 'POST'])
def reg():
   username = request.values.get('username').strip()
   password = request.values.get('password').strip()

   user = User.query.filter_by(username = username).first()
   if username == '' or password == '':
      return redirect_with_msg(url_for('regloginpage'), '用户名或密码为空！', 'relogin')

   if user != None:
      return redirect_with_msg(url_for('regloginpage'), '用户名已存在👌', 'relogin')

   # 将新用户入表
   salt = '.'.join(random.sample('0123456789abcdefgABCDEFG', 10))
   m = hashlib.md5()
   m.update(password.encode('utf-8') + salt.encode('utf-8'))
   password = m.hexdigest()
   user = User(username, password, salt)
   db.session.add(user)
   db.session.commit()

   return redirect('/')
   

   


@app.route('/legal/terms')
def legal_terms():
   pass

@app.route('/legal/privacy')
def legal_privacy():
   pass