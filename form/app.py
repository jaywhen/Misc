from flask import Flask, render_template, url_for

app = Flask(__name__)



@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/html')
def html():
   return render_template('pure_html.html')