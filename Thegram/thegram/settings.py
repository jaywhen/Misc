import os, sys
from thegram import app

WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'

dev_db = prefix + os.path.join(os.path.dirname(app.root_path), 'thegram.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', dev_db)
SECRET_KEY = os.getenv('SECRET_KEY', 'thegram')
ALLOWED_EXT = set(['png', 'jpg', 'jpeg', 'bmp', 'gif'])
UPLOAD_DIR = 'C:/Users/xiangjiewen/Desktop/upload/'

# SQLALCHEMY_DATABASE_URI = 'mysql://root@localhost/mydatabase'
# SQLALCHEMY_DATABASE_URI = 'sqlite:///../thegram.db'
