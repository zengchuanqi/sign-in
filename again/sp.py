import time

from selenium import webdriver




while True:
    time
    times = time.strftime('%H_%M', time.localtime(time.time()))
    if times =='22_52':
        wd=webdriver.Chrome()
        wd.get('https://baidu.com')
        break
    time.sleep(58)
