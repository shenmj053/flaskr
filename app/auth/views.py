#_*_coding: utf-8 _*_
from datetime import datetime
from flask import render_template, redirect, request, url_for, flash
from flask.ext.login import login_user
from flask.ext.login import logout_user, login_required
from . import auth
from ..models import User
from .forms import LoginForm,RegistrationForm
from .. import db

@auth.route('/register', methods=['GET', 'POST'])
def register():
    form  = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)
        db.session.add(user)
        flash('You can now login.')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form, current_time=datetime.utcnow())




@auth.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()  #用表单中填写的email从数据库中加载用户
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(request.args.get(next) or url_for('main.index'))
        flash('Invalid username or password')
    return render_template('auth/login.html', form=form, current_time=datetime.utcnow())

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('main.index'))