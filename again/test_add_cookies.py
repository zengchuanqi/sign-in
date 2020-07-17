from time import sleep

from selenium import webdriver


def test_cookies():
# wd = webdriver.Chrome()
# # cookie={'cookie':'BIDUPSID=BFA13255B1C105514DCC209DA1A142D7; PSTM=1584500503; BD_UPN=12314753; H_WISE_SIDS=144507_142018_144884_141748_144420_144135_142918_142780_144483_131247_137749_144741_138883_141942_127969_142874_140066_144337_140593_143058_141808_140351_144608_143468_144726_143922_131423_144277_128700_144005_107320_138595_139908_143596_143477_143472_143132_144239_143855_144098_143878_110085; BAIDUID=BFA13255B1C105514DCC209DA1A142D7:SL=0:NR=10:FG=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BDUSS=ZLaGppWGNnSmZndmhoNTVmYzJia3dvbHYyQmNwM1RRcFR4aWJsUmIwYUdmaHRmSVFBQUFBJCQAAAAAAAAAAAEAAACbVvjHxtXC3sPX0N7LuXpjdAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIbx816G8fNeam; shifen[173561585121_33854]=1593403832; shifen[172154411536_62169]=1593403840; BCLID=11234540747365279546; BDSFRCVID=n9KOJeC62m_hmpOuUfB-MZQEzgKacP7TH6aoaUYFcLzwrNI-jhyAEG0PSf8g0Kubp4PmogKK3gOTH48F_2uxOjjg8UtVJeC6EG0Ptf8g0f5; H_BDCLCKID_SF=tJKf_CIhtK-3f-op-P__jj_qhUKX5-RLfaA8bp7F5l8-hxoGhMI2hnLAbRJlWlTI36QMKKQ5aDOxOKQphnJVWlQDhbOIhxjtJC-O5J7N3KJmVnL9bT3v5tDtbpuq2-biWb7M2MbdJInP_IoG2Mn8M4bb3qOpBtQmJeTxoUJ25DnJhbLGe6KWjjJbeH08qbbfb-oEBnTM2Ru_Hn7zePIByU4pbt-qJtrd2Ijj2-5G5q_V8fchQJ6JyP_S0aJnBT5KaK6PhlQJBPcbqlrVqt6s2f_kQN3TQ-KO5bRiLRoMJUJVDn3oyTbJXp0nja7ly5jtMgOBBJ0yQ4b4OR5JjxonDh83bG7MJPKtfD7H3KC2fI-2bf5; BD_HOME=1; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; delPer=0; BD_CK_SAM=1; __yjsv5_shitong=1.0_7_c5a8a0cc030c6efec8e22eeb6618475538ac_300_1593433853420_119.134.100.152_a6961aa8; yjs_js_security_passport=ea9340135a79139e8807fb5e9b581c0861d46db8_1593433854_js; COOKIE_SESSION=30075_4_8_3_15_8_0_2_7_3_3_2_0_0_70_10_1593403901_1593403841_1593433906%7C9%23139430_579_1593403831%7C9; H_PS_PSSID=32193_1426_31672_21092_32139_31253_32046_32111_26350_22160; sug=3; sugstore=1; ORIGIN=0; bdime=0; PSINO=6; H_PS_645EC=b0ca%2BXOiEbtpYuBQfmO2DQ4t%2FpT8dtjOxBy6Y%2B6yUgHAZH%2FKu5itTTbw5rcAXLUW5XJh; BDSVRTM=0'}
#     wd.get('https://www.baidu.com/')
#     wd.add_cookie({'name':'COOKIE_SESSION','value':'30075_4_8_3_15_8_0_2_7_3_3_2_0_0_70_10_1593403901_1593403841_1593433906%7C9%23139430_579_1593403831%7C9'})
#     wd.add_cookie({'name':'BIDUPSID','value':'BFA13255B1C105514DCC209DA1A142D7'})
#     wd.add_cookie({'name':'BDUSS','value':'ZLaGppWGNnSmZndmhoNTVmYzJia3dvbHYyQmNwM1RRcFR4aWJsUmIwYUdmaHRmSVFBQUFBJCQAAAAAAAAAAAEAAACbVvjHxtXC3sPX0N7LuXpjdAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIbx816G8fNeam'})
#     sleep(2)
#     wd.refresh()  # 刷新
#     sleep(3)
#     cookies= wd.get_cookies()
#     print(cookies)
#     wd.quit()



    base_url = 'https://www.baidu.com/'
    browser = webdriver.Chrome()
    browser.get(base_url)

    # 1. 获取 cookie 信息
    cookies = browser.get_cookies()
    print(cookies)
    sleep(2)
    browser.quit()

    # 2. cookie 写入
    browser.add_cookie(
        {
            'name': 'add-cookie',
            'value': 'add-cookie-value'
        }
    )
    # 遍历cookies打印cookie信息
    for cookie in browser.get_cookies():
        print("%s ---> %s" % (cookie['name'], cookie['value']))
    sleep(2)
    browser.quit()