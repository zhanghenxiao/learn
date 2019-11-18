# -*- coding: utf-8 -*-
# @File    : falsk_test.py
# @Date    : 2019-10-12
# @Author  : Zhang.Cookie

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from yourapplication import db

"""

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()
"""

#使用flask 创建表，以管理员运行交互式
#参考链接：www.pythondoc.com/flask-sqlalchemy/quickstart.html  看文档


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123@localhost:3306/flask_news'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username



