import click
from thegram import app, db
from thegram.models import User, Image, Comment

import random

def get_image_url():
    return 'http://images.nowcoder.com/head/' + str(random.randint(0,1000)) + 'm.png'

@app.cli.command()
@click.option('--drop', is_flag=True, help='Create after drop')
def initdb(drop):
    """ initialize the database. """
    if drop:
        click.confirm('This operation will delete the database, do you want to continue?',abort=True)
        db.drop_all()
        click.echo('Database has been droped')
    db.create_all()
    click.echo('Initialized database')
    # add some user
    for i in range(0, 20):
        user = User(
            username = 'User' + str(i),
            password = 'a' + str(i)
        )
        db.session.add(user)

        for j in range(0, 6):
            image = Image(get_image_url(), i+1)
            db.session.add(image)

            for k in range(0, 3):
                comment = Comment(
                    content = '🧡' + str(k),
                    image_id = 1 + 6*i + j,
                    user_id = i + 1,
                ) 
                db.session.add(comment)

    db.session.commit()
    click.echo('now added some users')

@app.cli.command()
def tqur():
    """ do some test query """
    user = User.query.get(1)
    print(user.images)

    image = Image.query.get(1)
    print(image.user)

@app.cli.command()
def tupdate():
    """ do some test update """

    # 直接修改类属性名来实现数据库的update
    for i in range(50, 100, 2):
        user = User.query.get(i)
        user.username = '[VIP]' + user.username

    # 通过.update方法来实现数据库的update
    User.query.filter_by(id = 51).update({'username':'gimgon'})
    db.session.commit()

@app.cli.command()
def tdel():
    """ do some test delete """

    for i in range(50, 100, 2):
        comment = Comment.query.get(i+1)
        db.session.delete(comment)
    db.session.commit()