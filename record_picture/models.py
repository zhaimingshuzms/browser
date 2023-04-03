# -*- coding: utf-8 -*-
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from record_picture import db


# 用户个人信息表表
class User(db.Model, UserMixin):
    '''
    login_name:登陆账号
    id:账号id
    password_hash:账号密码
    profile_name:用户名,可修改
    iphone:电话号码,可修改
    country:国家,可修改
    picture_link:头像链接,可修改
    '''
    id = db.Column(db.Integer, primary_key=True)
    login_name = db.Column(db.String(20))
    password_hash = db.Column(db.String(128))
    profile_name = db.Column(db.String(20))
    iphone = db.Column(db.String(20))
    country = db.Column(db.String(20))
    picture_link = db.Column(db.String(100))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def validate_password(self, password):
        return check_password_hash(self.password_hash, password)


# 照片表
class Picture(db.Model):
    '''
    id:照片id(为唯一键)
    login_name:登陆账号
    picture_url:照片存储url
    title:照片标题
    '''
    id = db.Column(db.Integer, primary_key=True)
    login_name = db.Column(db.String(20))
    picture_url = db.Column(db.String(100))
    title = db.Column(db.String(20))
    scene = db.Column(db.String(200))

class Scene():
    def __init__(self, name, pictures):
        self.name = name
        self.pictures = pictures