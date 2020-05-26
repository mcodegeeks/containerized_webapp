from werkzeug.security import generate_password_hash, check_password_hash
from app import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), index=True, unique=True, nullable=False)
    username = db.Column(db.String(128), index=True, nullable=False)
    hashed_password = db.Column(db.String(128))

    def setPassword(self, password):
        self.hashed_password = generate_password_hash(password)

    def verifyPassword(self, password):
        return check_password_hash(self.hashed_password, password)

    def __repr__(self):
        return "User {{email: '{}', username: '{}'}}".format(self.email, self.username) 