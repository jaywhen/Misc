from thegram import app

from flask import render_template, url_for
from thegram.models import User, Image

@app.route('/')
def index():
   images = Image.query.order_by(Image.id.desc()).limit(10).all()
   return render_template('index.html', images = images)