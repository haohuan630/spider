#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/11 9:42
# @Author  : sunny
# @File    : views.py
# @Software: PyCharm

# -*- coding: utf-8 -*-
import datetime
import json
import os
import re

from lxml import etree
import requests

from spider import setting

path_add = os.path.dirname(os.path.realpath(__file__))
run_file = "上海信息经济委员会"


def get_news_info(news_info_url_list):
    """获取新闻信息"""
    for url_item in news_info_url_list:
        url = url_item
        # print(url)
        headers = setting.headers

        response = requests.get(url, headers=headers)
        news_info = response.text

        news_info = etree.HTML(news_info)
        news_info_id = url.split('/')[-1].split('.')[0]
        try:
            news_info_img = news_info.xpath('//*[@id="ivs_content"]/p/img/@src')
        except BaseException as e:
            print(e)
            news_info_img = ['']
        try:
            news_info_title = news_info.xpath('//*[@id="ivs_title"]/text()')
        except BaseException as e:
            print(e)
            news_info_title = ['']
        try:
            news_info_source = news_info.xpath('//div/h3[2]/text()')
        except BaseException as e:
            print(e)
            news_info_source = ['']
        try:
            news_info_content = news_info.xpath('//*[@id="ivs_content"]/p/text()')
        except BaseException as e:
            print(e)
            news_info_content = ['']

        # print(news_info, news_info_img)

        item = {}
        news_content = ''
        news_img = ''
        for con_item in news_info_content:
            news_content += con_item.replace(u'\xa0', u' ').replace(u'\u3000', '').replace(u'\r\n ', '').replace(u' ',
                                                                                                                 '') + '\r\n'

        for img_item in news_info_img:
            news_img += img_item + '\r\n'

        item['news_content'] = news_content
        item['news_img'] = news_img
        item['news_id'] = news_info_id
        item['news_title'] = news_info_title
        item['news_source'] = news_info_source
        item['news_url'] = str(url)
        item['spider_time'] = datetime.date.today()


def getDate(date):
    today = datetime.date.today()
    oneday = datetime.timedelta(days=date)
    yesterday = today - oneday
    day = str(yesterday).split('-')[-1]

    return day


def del_log():
    """删除日志"""
    # 删除七天的日志
    try:
        path = "./logs/log{}.txt".format(getDate(7))
        os.remove(path)
    except BaseException as e:
        print(e)


def save_log(item):
    """日志"""
    try:
        now_time = datetime.datetime.now()

        log_item = str(now_time) + '------' + str(item)
        path_file_name = './logs/log{}.txt'.format(getDate(0))

        if not os.path.exists(path_file_name):
            with open(path_file_name, "x") as f:
                pass

        with open(path_file_name, "a") as f:
            logs = json.dumps(log_item, ensure_ascii=False) + '\n'
            f.writelines(logs)
    except BaseException as e:
        print(e)


def news_info_main(item):
    # for url_item in news_url:

    for i in range(1, 3):
        if i != 1:
            url = setting.news_url.format(item, ('_' + str(i)))
        else:
            url = setting.news_url.format(item, '')

        headers = setting.headers
        # print(url)

        response = requests.get(url, headers=headers)
        news_info_HTML = response.text
        # print(news_info_HTML)

        rex = r'<p><a href="([^"]*)"[^>]*>([\s\S]*?)</a>'

        news_info_url_list = []
        for url_item in re.findall(rex, news_info_HTML):
            news_flag = url_item[0].split('/')[-2]
            if (news_flag == 'zxxx' or news_flag == 'ttxw'):
                news_info_url_list.append(url_item[0])

        get_news_info(news_info_url_list)


# @loggerInFile("sheitclog.txt", run_file, path_add)
def run():
    # 人员信息
    # spider_main()
    # 新闻动态
    # del_log()
    news_list = ['zxxx', 'ttxw']
    for item in news_list:
        news_info_main(item)


if __name__ == '__main__':
    # 上海经济和信息化委会
    run()
