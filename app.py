#!/usr/bin/env python
# coding=utf-8

from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return "home"


@app.route('/admin')
def home():
    return "admin"


if __name__ == '__main__':
    app.run(debug=True)
