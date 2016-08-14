from marshmallow import fields, Schema, post_load

from flask_wtf import Form

from wtforms import StringField, PasswordField, SubmitField

from wtforms.validators import DataRequired, EqualTo, Email

### User Registration ###

class RegForm(Form):
    user_name = StringField('Enter username', validators=[DataRequired()])
    password = PasswordField('Enter password', validators=[DataRequired()])
    email_id = StringField('Enter username', validators=[DataRequired(), Email('Email invalid')])
    submit = SubmitField('Submit')

class LoginForm(Form):
    user_name = StringField('Enter username', validators=[DataRequired()])
    password = PasswordField('Enter password', validators=[DataRequired()])
    submit = SubmitField('Submit')
######################


### Order registration ###

class OrderClass(object):

    def __init__(self, user, add, url, pri, qty):
        self.user_id = user
        self.address = add
        self.url = url
        self.price = pri
        self.quantity = qty


class OrderSchema(Schema):

    user_id = fields.Int()
    address = fields.Str()
    url = fields.Str()
    price = fields.Int()
    quantity = fields.Int()

    # @post_load
    # def make_order(self,data):
    #     return OrderClass(**data)

order_sch = OrderSchema()