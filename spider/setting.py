#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/10 16:02
# @Author  : sunny
# @File    : setting.py
# @Software: PyCharm


# mysql数据库相关配置
DATABASES = {
    'default': {
        'HOST': '192.168.11.97',
        'PORT': 3306,
        'USER': 'root',
        'PASSWORD': '123456',
        'DATABASE': 'spider',
        'CHARSET': 'utf8',
    }
}

# 注册APP installed // # 注册应用（应用名.apps.apps中的class）
INSTALLED_APPS = [
    'apps.sheitc.test',
    'apps.xinhua.test',
]
