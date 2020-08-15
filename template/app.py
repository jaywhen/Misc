from flask import Flask, render_template, flash, Markup

app = Flask(__name__)
app.secret_key = 'secret string'

user = {
    'username': 'Jaywhen',
    'bio': 'Love Haibara && Coding && basketball',
}

movies = [
    {'name': 'My Neighbor Totoro', 'year': '1988'},
    {'name': 'Three Colours trilogy', 'year': '1993'},
    {'name': 'Forrest Gump', 'year': '1994'},
    {'name': 'Perfect Blue', 'year': '1997'},
    {'name': 'The Matrix', 'year': '1999'},
    {'name': 'Memento', 'year': '2000'},
    {'name': 'The Bucket list', 'year': '2007'},
    {'name': 'Black Swan', 'year': '2010'},
    {'name': 'Gone Girl', 'year': '2014'},
    {'name': 'CoCo', 'year': '2017'},
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/watchlist')
def watchlist():
    return render_template('watchlist.html', user=user, movies=movies)

# register template context handler
@app.context_processor
def inject_info():
    foo = 'i am foo.'
    return dict(foo=foo) # equal to: return {'foo': foo}

# register template global function
@app.template_global()
def bar():
    return 'i am bar'

# register template filter
@app.template_filter()
def musical(s):
    return s + Markup(' &#9835;')

# register template test
@app.template_test()
def baz(n):
    if n == 'baz':
        return True
    return False


@app.route('/flash')
def just_flash():
    flash('flaaaaaaaaaaaaaaaaaaaaaaaaaaash')
    return redirect(url_for('index'))