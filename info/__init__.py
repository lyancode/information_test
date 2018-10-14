from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from redis import StrictRedis
# 可以用来指定Session保存的位置
from flask_session import Session
from config import config

# 初始化数据库
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)

    # 加载配置
    app.config.from_object(config[config_name])
    # 通过app初始化
    db.init_app(app)
    # 初始化redis存储对象
    redis_store = StrictRedis(host=config[config_name].REDIS_HOST, port=config[config_name].REDIS_PORT)
    # 开启当前项目CSRF保护
    CSRFProtect(app)
    # 设置session保存位置
    Session(app)

    return app
