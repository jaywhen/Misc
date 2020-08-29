from thegram import app

@app.route('/')
def index():
   return 'hello'