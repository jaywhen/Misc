from thegram import db

from datetime import datetime
import random
class User(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    username = db.Column(db.String(20), unique = True)
    password = db.Column(db.String(16))
    salt = db.Column(db.String(16))
    head_url = db.Column(db.String(256))
    images = db.relationship('Image', backref = 'user', lazy = 'dynamic')

    def __init__(self, username, password, salt = ''):
        self.username = username
        self.password = password
        self.salt = salt
        self.head_url = 'http://images.nowcoder.com/head/' + str(random.randint(0,1000)) + 'm.png'

    def __repr__(self):
        return '<User %d %s>' %(self.id, self.username)

class Image(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    url = db.Column(db.String(256)) 
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    created_date = db.Column(db.DateTime)
    comments = db.relationship('Comment')

    def __init__(self, url, user_id):
        self.url = url
        self.user_id = user_id
        self.created_date = datetime.now()

    def __repr__(self):
        return '<Image %d %s>' %(self.id, self.url)

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    content = db.Column(db.String(256))
    image_id = db.Column(db.Integer, db.ForeignKey(Image.id))
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    status = db.Column(db.Integer, default = 0) # 0正常 1被删
    user = db.relationship('User')

    def __init__(self, content, image_id, user_id):
        self.content = content
        self.image_id = image_id
        self.user_id = user_id

    def __repr__(self):
        return '<Comment %d %s>' %(self.id, self.content)

# 修改建表函数
# 尝试faker
# fake数据不要超过20个（user）




