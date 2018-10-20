from flask import render_template, request, jsonify, current_app, session, redirect, url_for

from info.models import User
from info.modules.admin import admin_blue
from info.utils.response_code import RET


@admin_blue.route('/index')
def index():
    return render_template('admin/index.html')



@admin_blue.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template('admin/login.html')

    # 取到登录的参数
    username = request.form.get("username")
    password = request.form.get("password")

    # 判断参数
    if not all([username, password]):
        # return jsonify(errno=RET.PARAMERR, errmsg="参数错误")
        return render_template('admin/login.html', errmsg="参数错误")

    # 查询当前用户
    try:
        user = User.query.filter(User.mobile==username, User.is_admin==True).first()
    except Exception as e:
        current_app.logger.error(e)
        return render_template('admin/login.html', errmsg="用户信息查询失败")

    if not user:
        return render_template('admin/login.html', errmsg="未查到用户信息")


    # 校验密码
    if not user.check_passowrd(password):
        return render_template('admin/login.html', errmsg="用户名或密码错误")

    # 保存用户的登录信息
    session["user_id"] = user.id
    session["mobile"] = user.mobile
    session["nick_name"] = user.nick_name
    session["is_admin"] = user.is_admin


    # 跳转到后台管理界面
    return redirect(url_for('admin.index'))
