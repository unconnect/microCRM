from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
from app.models import User


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    login = SubmitField('Sign in')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('E-Mail', validators=[DataRequired(), Email()])
    first_name = StringField('Firstname')
    last_name = StringField('Lastname')
    password = PasswordField('Password', validators=[DataRequired()])
    password_repeated = PasswordField('Repeat Password', validators=[
                                                DataRequired(),
                                                EqualTo('password')])
    submit = SubmitField('Register')

    def validate_user(self, username):
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None:
            raise ValidationError('This username is already registered. '
                                  'Please use a different one or try to login')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('This E-Mail address is already '
                                  'registered. Please use a different or try to login.')