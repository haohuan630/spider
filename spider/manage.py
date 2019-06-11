#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/10 16:02
# @Author  : sunny
# @File    : manage.py.py
# @Software: PyCharm
import importlib

from spider import setting


def main():
    """入口函数"""

    # BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    for app in setting.INSTALLED_APPS:
        # sys.path.insert(0, os.path.join(BASE_DIR, app.replace('.', "\\")))  # 添加导包路径
        try:
            execute_from_command = importlib.import_module(app)
            execute_from_command.run()
        except ImportError as exc:
            print(exc)


if __name__ == '__main__':
    main()
