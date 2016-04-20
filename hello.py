#_*_coding: utf-8 _*_

from flask import Flask
from flask import render_template
from flask import session
from flask import redirect
from flask import url_for
from flask import flash
from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
#from flask import request  #请求上下文
#from flask import redirect  #重定向
from datetime import datetime
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

app = Flask(__name__)

app.config['SECRET_KEY'] = 'hard to guess string'

manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)

class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():  #验证所提交的数据
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks you have changed your name!')
        session['name'] = form.name.data  #将数据存储在用户会话中
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'), current_time=datetime.utcnow())  #使用模板,加入datetime变量
    #return redirect ('https://www.baidu.com')  #重定向
    #user_agent = request.headers.get('User-Agent')
    #return '<p>Your Browser is %s</p>' % user-went

@app.route('/user/<name>')
def user(name):
    #return '<h1>Hello, %s!</h1>' % name
    return render_template('user.html', name=name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    #app.run(debug=True)
    manager.run()  #添加了命令行解释器