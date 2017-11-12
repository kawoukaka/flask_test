from flask import Blueprint, render_template, session, request, redirect, url_for
from ..models import users

home_blueprint = Blueprint('home_blueprint', __name__,template_folder='templates')

#home page
@home_blueprint.route('/home')
def home():
    try:
        if users.select().where(users.user_id == session['id']).count() == 1:
            username = users.select().where(users.user_id == session['id']).get().user_name
    except:
        return '''Database Error!'''

    return render_template('home.html',renderData=username)

@home_blueprint.route('/logout',methods=['POST'])
def logout():
    try:
        if session['id'] != None:
            users.update(user_status='offline').where(users.user_id==session['id'])
            session.pop('id', None)
            return redirect(url_for('index_blueprint.index'))
        else:
            return '''Already log out'''
    except:
        return '''Database Error!'''
    return redirect(url_for('index_blueprint.index'))
