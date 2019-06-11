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
    'apps.sheitc.views',
    'apps.shobserver.views',
    'apps.xinhua.views',
]

# 新闻分类
DATA_CLASS = {
    "http://www.sheitc.gov.cn/jgld/index.htm": 115,
    "https://www.shobserver.com": 216,
    "http://sh.xinhuanet.com/main/index.htm": 1,
    "http://sh.xinhuanet.com/shzw/index.htm": 2,
    "http://sh.xinhuanet.com/yq/index.htm": 3,
    "http://sh.xinhuanet.com/fortune/sclist.htm": 4,
    "http://sh.xinhuanet.com/fortune.html": 5,
    "http://sh.xinhuanet.com/fortune/jr.htm": 6,
    "http://sh.xinhuanet.com/fashion.html": 7,
    "http://sh.xinhuanet.com/tour.html": 8,
    "http://sh.xinhuanet.com/edu/wlist.htm": 9,
    "http://sh.xinhuanet.com/minsheng/index.htm": 10,
    "http://sh.xinhuanet.com/culture/index.htm": 11,
    "http://sh.xinhuanet.com/house/index.htm": 12,
    "http://sh.xinhuanet.com/sport/index.htm": 13,
    "http://sh.xinhuanet.com/health.html": 14
}

# 收件人邮箱设置
# RECEIVER = ['menghao.sun@grandhonor.net', 'honggang.wang@grandhonor.net']
RECEIVER = ['menghao.sun@grandhonor.net']
