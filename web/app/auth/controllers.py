from flask import render_template, redirect, url_for, flash
from flask_login import current_user, login_user
from app.auth import bp
from app.auth.views import LoginForm, RegisterForm, ForgotPasswordForm, ResetPasswordForm
from app.auth.models import User

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None:
            flash('Your email does not exist.')
            return redirect(url_for('auth.login'))
        elif not user.verifyPassword(form.password.data):
            flash('Your password is incorrect.')
            return redirect(url_for('auth.login'))
        login_user(user, remember=form.rememberMe.data)
        return redirect(url_for('main.index'))
    return render_template('login.html', title='Sign in', form=form)


@bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        flash('You have been registered successfully. Try signing in with it here.')
        return redirect(url_for('auth.login'))
    return render_template('register.html', title='Sign up', form=form)


@bp.route('/forgotpassword', methods=['GET', 'POST'])
def forgotPassword():
    form = ForgotPasswordForm()
    if form.validate_on_submit():
        return redirect(url_for('auth.resetPassword'))
    '''
    There was a problem
    We're sorry. We weren't able to identify you given the information provided.
    '''
    return render_template('forgot_password.html', title='Forgot password', form=form)


@bp.route('/resetpassword', methods=['GET', 'POST'])
def resetPassword():
    form = ResetPasswordForm()
    if form.validate_on_submit():
        flash('Your password has been changed successfully. Try signing in with it here.')
        return redirect(url_for('auth.login'))
    return render_template('reset_password.html', title='Reset password', form=form)
