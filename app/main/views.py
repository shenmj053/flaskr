#_*_coding: utf-8 _*_

from datetime import datetime
from flask import render_template, session, redirect, url_for, current_app

from . import main
from . forms import NameForm
from .. import db
from ..models import User
from ..email import send_email

@main.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():  #验证所提交的数据
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)  #将user加入数据库会话中
            session['known'] = False
            if current_app.config['FLASKY_ADMIN']:
                send_email(current_app.config['FLASKY_ADMIN'], 'new user', 'mail/new_user', user=user)
        else:
            session['known'] = True
        session['name'] = form.name.data  #将数据存储在用户会话中
        form.name.data = ''
        return redirect(url_for('.index'))
    return render_template('index.html', form=form, name=session.get('name'),
                           known=session.get('known', False), current_time=datetime.utcnow())