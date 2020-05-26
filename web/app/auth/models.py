from app import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), index=True, unique=True, nullable=False)
    username = db.Column(db.String(128), index=True, nullable=False)
    hashed_password = db.Column(db.String(128))

    def __repr__(self):
        return "User {{email: '{}', username: '{}'}}".format(self.email, self.username) 