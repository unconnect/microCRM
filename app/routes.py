from flask import render_template
from app import crm


@crm.route('/')
@crm.route('/index')
def index():
    # Dummy User with dictionary
    user = {'username': 'Nikolas'}
    customers = [
        {
            'company':  'Musterfirma 1 GmbH',
            'address':  'Musterstraße 1',
            'zipcode':  '12345',
            'city':     'Speckystädtchen',
            'creator': {'username': 'John'}
        },
        {
         'company': 'Musterfirma 2 GmbH',
            'address': 'Musterstraße 112',
            'zipcode': '54321',
            'city': 'Großstädtchen',
            'creator': {'username': 'Nikolas'}
        }
    ]

    return render_template('index.html', title="Homepage", user=user,
                           customers=customers)
