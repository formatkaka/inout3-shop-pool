from app import app, mail, api

from flask_restful import abort, Resource

from flask import make_response, request, jsonify, redirect, url_for, render_template

from .input_schemas import RegForm, LoginForm, order_sch

from .models import User

from .loction import get_distance

from flask_mail import Message



# import requests as r

@app.route('/test')
def test():
    message = '<h1> Hello, world ..Server is working </h1>'
    response = make_response(message)
    response.headers['content-type'] = 'text/html'
    # response.set_cookie('cookie.name','hello')
    #
    # val = request.cookies.get('cookie.name')

    return response

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegForm()

    if form.validate_on_submit():
        user = User.query.filter_by(user_name = form.user_name.data).first()
        if not user:
            token = User.add_user(form.user_name.data,
                          form.email_id.data,
                          form.password.data,
                          "dummy")
            response = make_response('<h2>logged in</h2>')
            response.set_cookie('session-id-inout', token)
            return response
        else:
            return 'ok'

    return render_template('register.html', form=form)

@app.route('/login',methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(user_name=form.user_name.data).first()
        if not user:
            return make_response('<h2>Invalid</h2>')
        else:
            response = make_response(redirect('loggedin'))
            response.set_cookie('session-id-inout', user.address)
            return response
    return render_template('login.html', form=form)

@app.route('/loggedin')
def loggedin():
    val = request.cookies.get('cookie.name')
    return 'logged in' + val

# class (Resource):
#
#     def get(self):
#         pass
#
#     def post(self):
#
#         user = request.authorization
#
#         if not user:
#             abort(400)
#
#         email = user.username
#         password = user.password
#
#         if not email or not password:
#             abort(400)
#
#         data, errors = user_reg.load(request.json())
#
#         token = User.add_user(data.username,
#                               email,
#                               password,
#                               data.address)
#
#         return token
#
#     def put(self):
#         pass
#
#     def delete(self):
#         pass


class AddToPool(Resource):

    def get(self):
        return jsonify({'here': 'ok'})

    def post(self):

        # print get_distance('svnit surat',50)
        print get_distance('bhabha bhavan svnit surat', 100)

        json_data = request.json
        # return json_data
        data, errors = order_sch.load(json_data)

        dist, addr, price_file = get_distance(data['address'], data['price'])

        print "here"
        print dist, addr, price_file

        if not dist or not addr or not price_file:
            return jsonify({'status':'no one in queue'})
        print data['user_id']
        user_sending = User.query.filter_by(id = 1).first()

        user = User.query.filter_by(id=3).first()

        print user_sending, user

        if not user_sending:
            abort(400, message='skdhg')

        else:
            if price_file > data['price']:

                low_user = user_sending.user_name
                low_email = user_sending.email_id
                high_user = user.user_name
                high_email = user.email_id

            else:
                low_user = user.user_name
                low_email = user.email_id
                high_user = user_sending.user_name
                high_email = user_sending.email_id

            msg_low = 'other user will book {0}'.format(low_email)
            msg_high = 'you book the order {0} '.format(high_email)

            send_email(msg_low, low_email)
            send_email(msg_high, high_email)
        return jsonify({'here':'ok'})

def send_email(msg1, email):
    msg = Message(subject='ShopPool', recipients=[email], sender='college.connect28@gmail.com')
    msg.body = msg1
    try:
        mail.send(msg)
    except Exception as e:
        print e
        abort(500)


api.add_resource(AddToPool, '/order' )