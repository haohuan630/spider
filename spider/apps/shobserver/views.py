#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/3 10:09
# @Author  : sunny
# @File    : views.py
# @Software: PyCharm
import datetime
import requests
from lxml import etree

from shobserver import setting
from spider.libs.log import loggerInFile
from spider.libs.utils import str_sub, str_replace
from spider.model.save_data_to_db import save_data
from spider.setting import DATA_CLASS

run_file = "上观-伴公汀"


def get_news_detail(news_url_list):
    """获取新闻详情页内容"""
    for news_url in news_url_list:
        # print(news_url)
        headers = setting.headers

        response = requests.get(news_url, headers=headers)
        news_info_HTML = response.text
        # print(news_info_HTML)
        news_info_etr = etree.HTML(news_info_HTML)

        news_id = news_url.split('=')[-1]

        news_title_xpa = news_info_etr.xpath('//div[@class="left"]/div[@class="wz_contents"]/text()')
        news_title = news_title_xpa[0] if news_title_xpa else ''

        news_abstract_xpa = news_info_etr.xpath('//div[@class="left"]/div[@class="wz_contents1"]/div[1]/text()')
        news_abstract = str_sub(news_abstract_xpa[1]) if news_abstract_xpa else ''

        news_content_xpa = news_info_etr.xpath(
            '//*[@id="newscontents"]//p/text() | //*[@id="newscontents"]//span/text()')
        news_content = ''
        for item in news_content_xpa:
            news_content = news_content + str_sub(item)

        news_publish_time_xpa = news_info_etr.xpath('//div[@class="left"]//div[@class="fenxiang_zz"]/text()')
        news_publish_time = str_replace(news_publish_time_xpa[2]).split('\t')[1] if news_publish_time_xpa else ''

        news_source_xpa = news_info_etr.xpath('//div[@class="left"]//div[@class="fenxiang_zz"]/span/text()')
        news_source = str_sub(news_source_xpa[0]) if news_source_xpa else ''
        news_author = news_source_xpa[1] if news_source_xpa else ''

        # //div[@class="con_ban"]/img/@src | //*[@id="newscontents"]/p/a/img/@src |'
        news_img_xpa = news_info_etr.xpath('//div[@class="con_ban"]/img/@src | //*[@id="newscontents"]/p/a/img/@src | '
                                           '//*[@id="newscontents"]/p/span/a/img/@src')
        news_img = ''
        for item in news_img_xpa:
            news_img = news_img + item + '\r\n'

        news_class = DATA_CLASS[setting.url]

        # print(news_author)
        news_dict = {}
        news_dict['news_id'] = news_id + "_2"
        news_dict['news_url'] = news_url
        news_dict['news_title'] = news_title
        news_dict['news_abstract'] = news_abstract
        news_dict['news_content'] = news_content
        news_dict['news_publish_time'] = news_publish_time
        news_dict['news_source'] = news_source
        news_dict['news_author'] = news_author
        news_dict['news_img'] = news_img
        news_dict['news_class'] = news_class
        news_dict['spider_time'] = datetime.date.today()

        # print(news_dict)
        save_data(news_dict)


def news_main():
    # for url_item in news_url:
    headers = setting.headers
    for page in range(1, 3):
        url_page = setting.url_page.format(page)
        # print(url_page)

        response = requests.get(url_page, headers=headers)
        news_info_HTML = response.text

        news_info_etr = etree.HTML(news_info_HTML)

        # //div[@class="chengshi"]//a/@href
        news_url_list = news_info_etr.xpath('//div[@class="chengshi"]//div[@class="chengshi_wz_h"]/a/@href')

        url_pre = setting.url
        news_url_list_pre = [url_pre + item for item in news_url_list]

        # print(len(news_url_list_pre))
        get_news_detail(news_url_list_pre)


@loggerInFile("shobserver_log.txt", run_file)
def run():
    news_main()


if __name__ == '__main__':
    # 上观-伴公汀
    run()
