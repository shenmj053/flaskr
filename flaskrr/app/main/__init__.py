#_*_coding: utf-8 _*_

from flask import Blueprint
#实例化Blueprint类来创建蓝本
main = Blueprint('main', __name__)
#导入路由和错误处理程序
from . import views, errors
from ..models import Permission

@main.app_context_processor
def inject_permission():
    return dict(Permission=Permission)