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
