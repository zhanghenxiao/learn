# -*- coding: utf-8 -*-
# @File    : falsk_test.py
# @Date    : 2019-10-12
# @Author  : Zhang.Cookie


from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()
