import click
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True, nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)

    def __init__(self, email):
        self.email = email

@app.route("/")
def index():
    return jsonify(hello="world")

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