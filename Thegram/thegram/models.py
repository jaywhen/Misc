from thegram import db
import random
class User(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    username = db.Column(db.String(20), unique = True)
    password = db.Column(db.String(16))
    head_url = db.Column(db.String(256))

    def __init__(self, username, password):
        self._username = username
        self._password = password
        self._head_url = 'http://images.nowcoder.com/head/' + str(random.randint(0,1000)) + 'm.png'

    def __repr__(self):
        return '<User %d %s>' %(self.id, self.username)
        


