import os
from flask import Flask, flash, render_template
from flask_mail import Mail



app = Flask(__name__)

app.config.update (
    MAIL_SERVER = os.getenv('MAIL_SERVER'),
    MAIL_PORT = 587,
    MAIL_USE_TLS = True,
    MAIL_USERNAME = os.getenv('MAIL_USERNAME'),
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD'),
    MAIL_DEFAULT_SENDER = ('MachineSo Team', os.getenv('MAIL_USERNAME'))
)

mail = Mail(app)

@app.route('/subscribe', methods = ['GET', 'POST'])
def subscribe():
   pass