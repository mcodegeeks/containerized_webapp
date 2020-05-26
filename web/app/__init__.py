from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from config import Config

db = SQLAlchemy()
bootstrap = Bootstrap()

def create_app(config_class=Config):
    app = Flask(__name__, template_folder="ui/templates")
    app.config.from_object(Config)

    db.init_app(app)
    bootstrap.init_app(app)

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.errors import bp as errors_bp
    app.register_blueprint(errors_bp)

    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp)

    return app


'''
import click

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
'''    