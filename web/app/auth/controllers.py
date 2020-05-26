from flask import render_template, redirect, url_for, flash
from app.auth import bp
from app.auth.views import LoginForm, RegisterForm, ForgotPasswordForm, ResetPasswordForm

@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
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
