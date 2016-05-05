#_*_coding: utf-8 _*_

import unittest
from flask import current_app
from app import create_app, db

class BasicsTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing') #'testing'为测试配置,导入后创建app实例
        self.app_context = self.app.app_context()  #激活上下文
        self.app_context.push()
        db.create_all()  #创建全新数据库

    #删除数据库和上下文
    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    #测试确保程序存在
    def test_app_exists(self):
        self.assertFalse(current_app is None)

    #确保程序在测试配置中进行
    def test_app_is_testing(self):
        self.assertTrue(current_app.config['TESTING'])