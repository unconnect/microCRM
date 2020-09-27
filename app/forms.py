from flask_wtf import FlaskForm
from wtforms import StringField, DateField, PasswordField, BooleanField, \
                                     SubmitField, TextAreaField
from wtforms.validators import DataRequired, InputRequired, ValidationError, \
    Email, \
    EqualTo, Length
from app.models import User


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    login = SubmitField('Sign in')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('E-Mail', validators=[DataRequired(), Email()])
    firstname = StringField('Firstname')
    lastname = StringField('Lastname')
    password = PasswordField('Password', validators=[DataRequired()])
    password_repeated = PasswordField('Repeat Password', validators=[
                                                DataRequired(),
                                                EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        """
        Overwrites the default Flask Validator,
        checks if username already in DB

        :raise: ValidationError
        """
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('This username is already registered. '
                                  'Please use a different one or try to login')

    def validate_email(self, email):
        """
        Overwrite the default Flask Validator, checks if email already in DB

        :raise: ValidationError
        """
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('This E-Mail address is already '
                                  'registered. Please use a different or try '
                                  'to login.')


class ProfileEditForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    # write method that checks if password is set and when, then validate
    # the fields, otherwise ignore them.

    email = StringField('E-Mail', validators=[DataRequired(), Email()])
    firstname = StringField('Firstname')
    lastname = StringField('Lastname')
    birthday = DateField('Birthday')
    entry_date = DateField('Entrydate')
    title = StringField('Title')
    info = TextAreaField('Information', validators=[Length(min=0, max=128)])
    submit = SubmitField('Submit')
