from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask('thegram')
app.config.from_pyfile('settings.py')
app.jinja_env.add_extension('jinja2.ext.loopcontrols')
db = SQLAlchemy(app)

from thegram import views, models, commands