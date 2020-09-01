from thegram import app

from flask import render_template, url_for, redirect
from thegram.models import User, Image

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