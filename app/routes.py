from flask import render_template
from app import crm
from datetime import date


@crm.route('/')
@crm.route('/index')
def index():
    # Dummy User with dictionary
    user = {'username': 'Nikolas'}
    theyear = date.today().year
    customers = [
        {
            'company':  'Musterfirma 1 GmbH',
            'address':  'Musterstraße 1',
            'zipcode':  '12345',
            'city':     'Speckystädtchen',
            'creator': {'username': 'John'}
        },
        {
         'company': 'Herbert und klein GbR',
            'address': 'Musterstraße 112',
            'zipcode': '54321',
            'city': 'Großstädtchen',
            'creator': {'username': 'Nikolas'}
        }
    ]

    return render_template('index.html',
                           title="Homepage",
                           user=user,
                           theyear=theyear,
                           customers=customers)