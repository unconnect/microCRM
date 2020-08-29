from flask import render_template, flash, redirect, url_for
from app import crm
from datetime import date
from app.forms import LoginForm

the_year = date.today().year


@crm.route('/')
@crm.route('/index')
def index():
    """
    Index View
    :return:
    """
    # Dummy User with dictionary
    user = {'username': 'Nikolas'}
    customers = [
        {
            'company': 'Musterfirma 1 GmbH',
            'address': 'Musterstraße 1',
            'zipcode': '12345',
            'city': 'Speckystädtchen',
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
                           the_year=the_year,
                           customers=customers)


@crm.route('/login', methods=['GET', 'POST'])
def login():
    """
    Login View
    :return:
    """
    form = LoginForm()

    # When User is valid show flash message and redirect to /index
    if form.validate_on_submit():
        flash(f'Login requested for user {form.username.data},'
              f'remember_me={form.remember_me.data}')
        return redirect(url_for('index'))
    return render_template('login.html',
                           title='Sign In',
                           the_year=the_year,
                           form=form)
