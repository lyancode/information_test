import logging

from flask import session
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from info import create_app, db

# 通过指定的配置名字创建对应配置的app
app = create_app("development")
manager = Manager(app)
# 将app与db关联
Migrate(app, db)
# 将迁移命令添加到manager中
manager.add_command("db", MigrateCommand)


@app.route('/')
def index():
    # session["name"] = "mark"

    # 测试打印日志
    logging.debug("DEBUG")
    logging.warning("WARRING")
    logging.error("ERROR")
    logging.fatal("FATAL")

    return 'Hello World2333'


if __name__ == '__main__':
    manager.run()
