import click
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify(hello="world")

@app.cli.command('create')
@click.argument('args')
def create(args): 
    """Create an initial database for 'db' argument."""
    if (arg == 'db'):
        print("creating db")
    else:
        print("Usage: flask [OPTIONS] COMMAND [ARGS]...\n" \
              "Try 'flask --help' for help.\n\n" \
              "Error: No such argument '%s'." % args)

if __name__ == "__main__":
    app.run()