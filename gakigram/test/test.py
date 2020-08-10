from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1 style="color : rebeccapurple;">Hello, Jaywhen</h1>'

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s!</h1>' % name

@app.route('/fans/<int:number>')
def t(number):
    return render_template('test.html', num = number)

 
if __name__ == '__main__':
    app.run(debug=True)