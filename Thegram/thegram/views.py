from thegram import app

from flask import render_template, url_for, redirect, request, flash
from thegram.models import User, Image
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

@app.route('/login')
def login():
   return render_template('login.html')

@app.route('/reg')
def reg():
   username = request.values.get('username').strip()
   password = request.values.get('password').strip()

   user = User.query.filter_by(username = username).first()
   if username == '' or password == '':
      redirect_with_msg(url_for('login'), '用户名或密码为空！', 'login')

   if user != None:
      redirect_with_msg(url_for('login'), '用户名已存在👌', 'login')

   # 将新用户入表

   


@app.route('/legal/terms')
def legal_terms():
   pass

@app.route('/legal/privacy')
def legal_privacy():
   pass