#_*_coding: utf-8 _*_

from flask import Flask
from flask.ext.script import Manager
from flask import render_template
#from flask import request  #请求上下文
#from flask import redirect  #重定向

app = Flask(__name__)
manager = Manager(app)  #
@app.route('/')
def index():
    #return '<h1>Hello World!</h1>'
    return render_template('index.html')  #使用模板
    #return redirect ('https://www.baidu.com')  #重定向
    #user_agent = request.headers.get('User-Agent')
    #return '<p>Your Browser is %s</p>' % user-went

@app.route('/user/<name>')
def user(name):
    #return '<h1>Hello, %s!</h1>' % name
    return render_template('user.html', name=name)

if __name__ == '__main__':
    #app.run(debug=True)
    manager.run()  #添加了命令行解释器