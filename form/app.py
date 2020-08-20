import os
from flask import Flask, render_template, url_for, flash, redirect
from forms import LoginForm, UploadForm

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'secret string')
app.config['UPLOAD_PATH']

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/basic', methods=['GET', 'POST'])
def basic():
   form = LoginForm()
   if form.validate_on_submit():
      username = form.username.data
      flash('Welcome home! %s !' % username)
      return redirect(url_for('index'))
   return render_template('basic.html', form = form)

@app.route('/html')
def html():
   return render_template('pure_html.html')

@app.route('/bootstrap', methods=['GET', 'POST'])
def bootstrap():
    form = LoginForm()
    return render_template('bootstrap.html', form=form)

@app.route('/test')
def test():
   return render_template('jaywhenbase.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
   form = UploadForm()
