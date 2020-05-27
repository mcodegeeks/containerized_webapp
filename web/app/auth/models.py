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

    def setPassword(self, password):
        self.hashed_password = generate_password_hash(password)

    def verifyPassword(self, password):
        return check_password_hash(self.hashed_password, password)

    def getResetPasswordToken(self, expires=120):
        return jwt.encode({'resetpassword': self.id, 'exp': time() + expires},
                          current_app.config['SECRET_KEY'], algorithm='HS256').decode('utf-8')

    @staticmethod
    def verifyResetPasswordToken(token):
        try:
            id = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])['resetpassword']
        except:
            return
        return User.query.get(id)        

@login.user_loader
def getUserById(id):
    return User.query.get(int(id))