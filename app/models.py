from app import db
from app import login
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from hashlib import md5


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class User(UserMixin, db.Model):
    # __tablename__ = 'custom_table_name'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    firstname = db.Column(db.String(64))
    lastname = db.Column(db.String(64))
    email = db.Column(db.String(255), index=True, unique=True)
    birthday = db.Column(db.Date)
    entry_date = db.Column(db.Date)
    title = db.Column(db.String(64))
    info = db.Column(db.String(128))
    password_hash = db.Column(db.String(128))
    customers = db.relationship('Customer', backref='creator', lazy='dynamic')
    last_login = db.Column(db.DateTime, default=datetime.utcnow)

    # Constructor
    def __init__(self, username, email, firstname, lastname):
        self.username = username
        self.email = email
        self.firstname = firstname
        self.lastname = lastname

    # Object representation in console prints etc.
    def __repr__(self):
        return f'<User {self.username}>'

    def set_password(self, password):
        """
        Generates and sets user password hash for given password.

        :param password:
        """
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def avatar(self, size):
        """
        Generates profil image

        :param size:
        :return: image-url
        """
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return f'https://www.gravatar.com/avatar/{digest}?d=identicon&s={size}'


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(255))
    address = db.Column(db.String(255))
    zipcode = db.Column(db.String(5))
    city = db.Column(db.String(64))
    creator_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    created = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return f'<Customer {self.company}'
