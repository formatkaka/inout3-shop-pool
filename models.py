from app import db
from app import app

from flask_restful import abort

import time

from .db_manager import add_to_db

#################
#### MODELS #####
#################

class User(db.Model):
    """ User reg table """
    __tablename__ = 'user'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String, unique=True, nullable=False)
    email_id = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    address = db.Column(db.String)
    orders = db.relationship('Orders', backref='my_user', lazy='dynamic')


    @staticmethod
    def add_user(*args):
        user = User(user_name=args[0],
                    email_id=args[1],
                    password = args[2],
                    address = args[3])

        if add_to_db(user):
            return user.auth_token()

    def auth_token(self):
        return self.email_id


class Orders(db.Model):
    """ orders by a user """
    __tablename__ = 'orders'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    order_name = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    order_meta = db.relationship('OrdersMeta', backref='order', lazy='dynamic')
    time_received = db.Column(db.Float, default=time.time())
    order_url = db.Column(db.String)
    order_dealer = db.Column(db.String)

class OrdersMeta(db.Model):
    """meta data for an order """
    __tablename__ = 'orders_meta'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    meta_about = db.Column(db.String)
    meta_value = db.Column(db.String)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'))


