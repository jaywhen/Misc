from flask import Flask
import click

app = Flask(__name__)

@app.route('/')
@app.route('/egg')
def index():
    return '<h1>恕瑞玛，你们的皇帝回来了！</h1>'

@app.cli.command()
def hello():
    """ say hello """
    click.echo('Hi! Jaywhen!')
    