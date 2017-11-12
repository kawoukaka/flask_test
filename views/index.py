from flask import Blueprint, render_template, session, request, redirect, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from ..models import users
import os
index_blueprint = Blueprint('index_blueprint', __name__,template_folder='templates')

#index page
@index_blueprint.route('/')
def index():
    return render_template('index.html')

#register
@index_blueprint.route('/join')
def join():
    return render_template('join.html')

#register user
@index_blueprint.route('/register',methods=['POST'])
def register():
    if request.method == 'POST':
        if users.select().where(users.user_name == request.form['username']).count() < 1:
            #user password encryted
            users.create(user_name=request.form['username'],
                         user_password=generate_password_hash(request.form['password']),
                         user_accesskey=os.urandom(24))
            return redirect(url_for('index_blueprint.index'))
        else:
            return '''User Already Existed '''
    return

#login
@index_blueprint.route('/login',methods=['POST'])
def login():

    if request.method == 'POST':
        if users.select().where(users.user_name==request.form['username']).count() == 1:
            user = users.select().where(users.user_name==request.form['username']).first()
            if check_password_hash(user.user_password,request.form['password']):
                session['key'] = user.user_accesskey
                user.update(user_status='online').where(user.user_id==session['key'])
                return redirect(url_for('home_blueprint.home'))
            else:
                return ''' Invalid Password! '''
        else:
            return ''' Invalid User Name! '''
    return
