#!/usr/bin/env Python
# coding=utf-8
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import time

from selenium import webdriver


wd=webdriver.Chrome()
wd.get('https://www.baidu.com')
print('ok')
wd.quit()
