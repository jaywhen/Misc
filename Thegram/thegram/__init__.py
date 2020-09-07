from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
app = Flask('thegram')
app.config.from_pyfile('settings.py')
app.jinja_env.add_extension('jinja2.ext.loopcontrols')
db = SQLAlchemy(app)
login_manager = LoginManager(app)

# 自定义跳转登录页
login_manager.login_view = '/regloginpage'

from thegram import views, models, commands