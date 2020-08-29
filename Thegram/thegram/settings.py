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



# SQLALCHEMY_DATABASE_URI = 'mysql://root@localhost/mydatabase'
# SQLALCHEMY_DATABASE_URI = 'sqlite:///../thegram.db'
