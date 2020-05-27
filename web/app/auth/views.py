from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.auth.models import User

class LoginForm(FlaskForm):
    email = StringField('E-mail address', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign-In')    
    rememberMe = BooleanField('Keep me signed in.')

class RegisterForm(FlaskForm):
    email = StringField('E-mail address', validators=[DataRequired(), Email()])
    username = StringField('Your name', validators=[DataRequired()])    
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Create your account')

    def validate_email(self, field):
        user = User.query.filter_by(email=field.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')

    def validate_password(self, field):
        if len(field.data) < 6:
            raise ValidationError('Passwords must consist of at least 6 characters.')

class ForgotPasswordForm(FlaskForm):
    email = StringField('E-mail address', validators=[DataRequired(), Email()])
    submit = SubmitField('Continue')

class ResetPasswordForm(FlaskForm):
    password = PasswordField('New password', validators=[DataRequired()])
    password2 = PasswordField('Password again', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Save changes and sign in')

    def validate_password(self, field):
        if len(field.data) < 6:
            raise ValidationError('Passwords must consist of at least 6 characters.')    