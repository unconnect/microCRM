from flask import render_template, flash, redirect, url_for, request
from app import crm, db
from datetime import date
from app.forms import LoginForm, RegistrationForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User
from werkzeug.urls import url_parse

the_year = date.today().year


@crm.route('/')
@crm.route('/index')
@login_required
def index():
    """
    Index View:
    Shows the apps dashboard for logged in users.

    :return: render_template()
    """
    # Dummy User with dictionary
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
                           the_year=the_year,
                           customers=customers)


@crm.route('/login', methods=['GET', 'POST'])
def login():
    """
    Login View:
    Renders login form and verifies user credentials. Redirects to index after
    user successfully logged in and flashes a message. Otherwise renders the
    form again.

    :return: redirect()
    """
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    # When User is valid show flash message and redirect to /index
    if form.validate_on_submit():
        # Gets User by username and returns the first entry in query. In
        # this case one or none user.
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password!')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html',
                           title='Sign In',
                           the_year=the_year,
                           form=form)


@crm.route('/logout')
def logout():
    """
    Logout the logged in user
    :return: redirect()
    """
    logout_user()
    return redirect(url_for('index'))


@crm.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data,
                    email=form.email.data,
                    firstname=form.firstname.data,
                    lastname=form.lastname.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('You have successfully registered!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form,
                           the_year=the_year)
