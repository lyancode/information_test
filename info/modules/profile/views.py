from flask import render_template, g, redirect, request, jsonify
from sqlalchemy.sql.functions import user

from info.modules.profile import profile_blue
from info.utils.common import user_login_data
from info.utils.response_code import RET


@profile_blue.route('/pic_info', methods=['POST', 'GET'])
@user_login_data
def pic_info():
    if request.method == "GET":
        return render_template('news/user_pic_info.html', data={"user": g.user.to_dict()})

    # TODO 如果是post表示是修改头像


@profile_blue.route('/base_info', methods=['POST', 'GET'])
@user_login_data
def base_info():
    # 不同的请求方式，做不同的事情
    if request.method == "GET":
        return render_template('news/user_base_info.html', data={"user": g.user.to_dict()})

    # 代表修改用户数据
    # 1、取到传入的参数
    nick_name = request.json.get("nick_name")
    signature = request.json.get("signature")
    gender = request.json.get("gender")

    # 2、检验参数
    if not all([nick_name, signature, gender]):
        return jsonify(errno=RET.PARAMERR, errmsg="参数错误")
    if gender not in ["MAN", "WOMAN"]:
        return jsonify(errno=RET.PARAMERR, errmsg="参数错误")

    user = g.user
    user.nick_name = nick_name
    user.signature = signature
    user.gender = gender

    return jsonify(errno=RET.OK, errmsg="OK")


@profile_blue.route('/info')
@user_login_data
def user_info():
    user = g.user
    if not user:
        # 代表没有登录，重定向到首页
        return redirect('/')
    data = {"user": user.to_dict()}
    return render_template('news/user.html', data=data)
