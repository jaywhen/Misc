from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask('thegram')
app.config.from_pyfile('settings.py')
db = SQLAlchemy(app)

from thegram import views, models, commands