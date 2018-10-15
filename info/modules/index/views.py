from flask import render_template, current_app

from info import redis_store
from . import index_blue


@index_blue.route('/')
def index():
    return render_template('news/index.html')


# send_static_file是flask查找指定的静态文件的方法
@index_blue.route('/favicon.ico')
def favicon():
    return current_app.send_static_file('news/favicon.ico')
