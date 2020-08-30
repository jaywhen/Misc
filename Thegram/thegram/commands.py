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
    for i in range(0, 3):
        user = User(
            username = 'User' + str(i),
            password = 'a' + str(i)
        )
        db.session.add(user)

        for j in range(0, 2):
            image = Image(get_image_url(), i+1)
            db.session.add(image)

            for k in range(0, 2):
                comment = Comment(
                    content = 'This is a test comment' + str(k),
                    image_id = 1 + 2*i + j,
                    user_id = i + 1
                ) 
                db.session.add(comment)

    db.session.commit()
    click.echo('now added some users')

@app.cli.command()
def tcli():
    """ for testing """
    print('hi')