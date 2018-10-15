from flask import render_template

from info import redis_store
from . import index_blue


@index_blue.route('/')
def index():
    return render_template('news/index.html')
