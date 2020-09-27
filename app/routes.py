from flask import render_template, flash, redirect, url_for, request
from app import crm, db
from datetime import date, datetime
from app.forms import LoginForm, RegistrationForm, ProfileEditForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, Customer
from werkzeug.urls import url_parse

the_year = date.today().year


@crm.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_login = datetime.utcnow()
        db.session.commit()


@crm.route('/')
@crm.route('/index')
@login_required
def index():
    """
    Shows the apps dashboard for logged in users.

    :return: render_template()
    """
    customers = Customer.query.all()
    return render_template('index.html',
                           title="Homepage",
                           the_year=the_year,
                           customers=customers)


@crm.route('/login', methods=['GET', 'POST'])
def login():
    """
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
    """
    Register a new user.

    :return: if form validates - redirect
    else render_template
    """
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
    return render_template('register.html',
                           title='Register',
                           form=form,
                           the_year=the_year)


@crm.route('/user/<username>')
@login_required
def user(username):
    """
    Renders the users profile page with a list of created customers.

    :param username:
    :return: render_template
    """
    user = User.query.filter_by(username=username).first_or_404()
    customers = Customer.query.filter_by(creator=user).all()
    return render_template('user.html',
                           title='Profile',
                           user=user,
                           customers=customers)


@crm.route('/user/edit/<username>', methods=['GET', 'POST'])
@login_required
def user_edit(username):
    form = ProfileEditForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        current_user.firstname = form.firstname.data
        current_user.lastname = form.lastname.data
        current_user.info = form.info.data
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('user_edit', username=username))
    elif request.method == 'POST':
        flash('Something went wrong!')
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
        form.firstname.data = current_user.firstname
        form.lastname.data = current_user.lastname
        form.info.data = current_user.info
    return render_template('user_edit.html',
                                   title='Profile Edit',
                                   form=form)