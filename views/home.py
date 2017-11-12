from flask import Blueprint, render_template, session, request, redirect, url_for
from ..models import users

home_blueprint = Blueprint('home_blueprint', __name__,template_folder='templates')

#home page
@home_blueprint.route('/home')
def home():
    try:
        if users.select().where(users.user_accesskey == session['key']).count() == 1:
            username = users.select().where(users.user_accesskey == session['key']).get().user_name
    except:
        return '''Database Error!'''

    return render_template('home.html',renderData=username)

@home_blueprint.route('/logout',methods=['POST'])
def logout():
    try:
        if session['key'] != None:
            users.update(user_status='offline').where(users.user_id==session['key'])
            session.pop('key', None)
            return redirect(url_for('index_blueprint.index'))
        else:
            return '''Already log out'''
    except:
        return '''Database Error!'''
    return redirect(url_for('index_blueprint.index'))
