from flask_wtf import CSRFProtect
from redis import StrictRedis
from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
# 可以用来指定Session保存的位置
from flask_session import Session
from flask_script import Manager


class Config(object):
    """项目的配置"""
    DEBUG = True
    SECRET_KEY = "7S04rmpWCcwlK4zPwDH1hScf876FASCAqXpxmLj/E8hoaUQpcCEJ1M0bbCBlClF1"

    # 为数据库添加配置
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://root:root@127.0.0.1:3306/information"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # redis的配置
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379
    REDIS_PASSWORD = "root"

    # session保存配置
    SESSION_TYPE = "redis"
    # 开启session签名
    SESSION_USE_SIGNER = True
    # 指代session 保存的 redis
    SESSION_REDIS = StrictRedis(host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD)
    # 设置需要过期
    SESSION_PERMANENT = False
    # 设置过期时间
    PERMANENT_SESSION_LIFETIME = 86400 * 2


app = Flask(__name__)

# 加载配置
app.config.from_object(Config)

# 初始化数据库
db = SQLAlchemy(app)
# 初始化redis存储对象
redis_store = StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)
# 开启当前项目CSRF保护
CSRFProtect(app)
# 设置session保存位置
Session(app)

manager = Manager(app)


@app.route('/')
def index():
    session['name'] = "zhangsan"
    return 'Hello World'


if __name__ == '__main__':
   manager.run()
