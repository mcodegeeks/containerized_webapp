from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo

class LoginForm(FlaskForm):
    email = StringField('E-mail address', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign-In')    
    rememberMe = BooleanField('Keep me signed in.')

class RegisterForm(FlaskForm):
    username = StringField('Your name', validators=[DataRequired()])
    email = StringField('E-mail address', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Create your account')

    '''
    Passwords must consist of at least 6 characters.
    '''

class ForgotPasswordForm(FlaskForm):
    email = StringField('E-mail address', validators=[DataRequired(), Email()])
    submit = SubmitField('Continue')

class ResetPasswordForm(FlaskForm):
    password = PasswordField('New password', validators=[DataRequired()])
    password2 = PasswordField('Password again', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Save changes and sign in')