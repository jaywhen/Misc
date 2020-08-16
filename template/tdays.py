from flask import Flask, request, redirect
app = Flask(__name__)



@app.route('/')
def index():
   return '<h1>you are in home page!</h1>'

@app.route('/hello')
def hello():
    # 第二个参数为默认值，若仅有/hello则为Hello！Flask
   name = request.args.get('name', 'Flask')
   return '<h1>Hello! %s</h>' % name


# 重定向
@app.route('/re')
def re():
   return '', 302, {'Location': 'http://www.example.com'}

# 重定向，更好的方式
@app.route('/rel')
def rel():
    return redirect('http://www.example.com')
   