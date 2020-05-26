import click
from app import create_app, db
from app.auth.models import User

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User}
    # u = User(email='susan@example.com', username='susan')

@app.cli.command('create')
@click.argument('args')
def create(args): 
    """Create a database with initial data for 'database' argument."""
    if (args == 'database'):
        print("Creating database")
        db.drop_all()
        db.create_all()
        db.session.commit()
    else:
        print("Usage: flask [OPTIONS] COMMAND [ARGS]...\n" \
              "Try 'flask --help' for help.\n\n" \
              "Error: No such argument '%s'." % args)  

if __name__ == "__main__":
    app.run()