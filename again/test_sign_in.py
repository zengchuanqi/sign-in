import smtplib
from email.mime.text import MIMEText
from email.header import Header
import os
from time import sleep
from selenium import webdriver

def send_email(context):
    sender = 'zengchuantu@163.com'
    # 接收邮箱
    receiver = '1501327456@qq.com'
    # 发送邮件主题
    subject = '报告'
    # 发送邮箱服务器
    smtpserver = 'smtp.163.com'
    # 发送邮箱用户/密码
    print(context)
    username = 'zengchuantu@163.com'
    password = 'FCXFCQQEIPAPGVWF'
    # 中文需参数‘utf-8’，单字节字符不需要
    msg = MIMEText(context, 'html', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')
    msg['from'] = sender
    msg['to'] = receiver
    smtp = smtplib.SMTP()
    smtp.connect('smtp.163.com')
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()

try:
    driver = webdriver.Chrome()
    driver.get('https://www.wnflb66.com/forum.php')
    driver.implicitly_wait(10)
    driver.find_element_by_css_selector('tr:nth-child(2)  .fastlg_l').click()
    driver.find_element_by_name('username').send_keys('1501327456@qq.com')
    driver.find_element_by_name('password').send_keys('zct123580')
    driver.find_element_by_css_selector('.fastlg_l [type=submit]').click()
    driver.find_element_by_id('fx_checkin_topb').click()
    send_email('<h1>fuliba打卡成功<h1>')
    driver.quit()
except:
    send_email('<h1>fuliba打卡失败<h1>')