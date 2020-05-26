from flask import render_template, redirect, url_for, flash
from app.auth import bp
from app.auth.views import RegisterForm

@bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('main.index'))
    return render_template('register.html', title='Register', form=form)