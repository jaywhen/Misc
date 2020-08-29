import click
from thegram import app, db

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

@app.cli.command()
def tcli():
    print('hi')