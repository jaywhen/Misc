import os
from flask import Flask, render_template, url_for
from forms import LoginForm

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'secret string')


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/basic')
def basic():
   form = LoginForm()
   return render_template('basic.html', form = form)

@app.route('/html')
def html():
   return render_template('pure_html.html')

@app.route('/bootstrap', methods=['GET', 'POST'])
def bootstrap():
    form = LoginForm()
    return render_template('bootstrap.html', form=form)