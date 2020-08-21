import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, flash, url_for, redirect

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'secret string')

app.config['SQLALCHEMY_DATABASE URI'] = \
os.getenv('DATABASE_URL', 'sqlite:///' + os.path.join(app.root_path, 'data.db'))

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
