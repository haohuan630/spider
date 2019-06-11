#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/3 10:09
# @Author  : sunny
# @File    : setting.py
# @Software: PyCharm

url = 'https://www.shobserver.com'
url_page = 'https://www.shobserver.com/news/sublist?section=2&page={}'


# 请求头
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,fr;q=0.7,ja;q=0.6",
    "Content-Type": "text/html;charset=utf-8",
    "Host": "www.shobserver.com",
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
}

# mysql数据库相关配置
MYSQL_HOST = '192.168.11.97'
MYSQL_PORT = 3306
MYSQL_DB = 'spider'
MYSQL_USER = 'root'
MYSQL_PASSWD = '123456'
CHARSET = 'utf8'


