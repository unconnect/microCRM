from app import db
from datetime import datetime


class User(db.Model):
    # __tablename__ = 'custom_table_name'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(255), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    customers = db.relationship('Customer', backref='creator', lazy='dynamic')

    def __repr__(self):
        return f'<User {self.username}>'


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
