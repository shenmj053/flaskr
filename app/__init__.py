#_*_coding: utf-8 _*_

#程序包的构造文件
from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.mail import Mail
#从配置文件config.py中导入config字典
from config import config
#移到下面的函数中,延迟创建
#app = Flask(__name__)

bootstrap = Bootstrap()
moment = Moment()
db = SQLAlchemy()
mail = Mail()

def create_app(config_name):
    #将第9行的创建程序实例移过来,从而延迟创建
    app = Flask(__name__)
    #从config字典中导入配置
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)

    from .main import main as main_blueprint
    #注册蓝本
    app.register_blueprint(main_blueprint)

    #工厂函数返回创建的程序实例,程序时在运行时创建的
    return app
