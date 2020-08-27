from flask import render_template
from app import crm


@crm.route('/')
@crm.route('/index')
def index():
    # Dummy User with dictionary
    user = {'username': 'Nikolas'}
    return render_template('index.html', user=user)