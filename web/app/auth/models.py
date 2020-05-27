import jwt
from time import time
from flask import current_app
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db, login

class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), index=True, unique=True, nullable=False)
    username = db.Column(db.String(128), index=True, nullable=False)
    hashed_password = db.Column(db.String(128))

    def __repr__(self):
        return "User {{email: '{}', username: '{}'}}".format(self.email, self.username)

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def validate_password(self, password):
        return check_password_hash(self.hashed_password, password)

    def get_reset_password_token(self, expires=120):
        return jwt.encode({'reset_password': self.id, 'exp': time() + expires},
                          current_app.config['SECRET_KEY'], algorithm='HS256').decode('utf-8')

    @staticmethod
    def validate_reset_password_token(token):
        try:
            id = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])['reset_password']
        except:
            return
        return User.query.get(id)        

@login.user_loader
def get_user(id):
    return User.query.get(int(id))