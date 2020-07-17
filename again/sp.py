import time

from selenium import webdriver


wd=webdriver.Chrome()
wd.get('https://www.baidu.com')
print('ok')
wd.quit()
