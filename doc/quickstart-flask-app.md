### Prerequisite
- Make sure that the python3 package is installed.
- Change a working directory

### Create a virtual environment
```
$ python3 -m venv venv
```

### Activate the virtual environment
- Regardless of which version of Python you are using, when the virtual environment is activated, you should use the pip command (not pip3)
```
$ source venv/bin/activate
```

### Upgrage python package installer 
```
(venv) $ pip install --upgrade pip
```

### Install flask framework
```
(venv) $ pip install flask
```

### Freeze installed packages in requirements format
```
(venv) $ pip freeze > requirements
```

### Install dependecies from requirements file
```
(venv) $ pip install -r requirements
```

### Deactivate the virtual environment
```
(venv) $ deactivate
```

### Creating the Web Server Gateway Interface (WSGI) Entry Point (wsgi.py)
```
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify(hello="world")

if __name__ == "__main__":
    app.run()
```

### Run the flask app
```
(venv) $ flask run 
```

### Navigate to http://localhost:5000/. You should see:
```
{"hello":"world"}
```

### Packages
```
(venv) $ pip install flask                  # A simple framework for building complex web applications.
(venv) $ pip install python-dotenv          # Add .env support to your flask apps in development and deployments
(venv) $ pip install Jinja2                 # A very fast and expressive template engine.
(venv) $ pip install flask-wtf              # Simple integration of Flask and WTForms.
(venv) $ pip install email-validator        # A robust email syntax and deliverability validation library for Python 2.x/3.x.
(venv) $ pip install flask-sqlalchemy       # Adds SQLAlchemy support to your Flask application.
(venv) $ pip install SQLAlchemy             # Database Abstraction Library
(venv) $ pip install flask-migrate          # SQLAlchemy database migrations for Flask applications using Alembic
```

### Database Migration
```
(venv) $ flask db [OPTIONS] COMMAND [ARGS]  # Perform database migrations.
(venv) $ flask db init                      # Creates a new migration repository.
(venv) $ flask db migrate -m "users table"  # Autogenerate a new revision file (Alias for 'revision...
(venv) $ flask db upgrade                   # Upgrade to a later version
(venv) $ flask db downgrade                 # Revert to a previous version
```
