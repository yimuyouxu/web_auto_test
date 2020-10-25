# coding=utf-8

from selenium import webdriver
import datetime
import time


def login():
    driver.get("https://www.taobao.com")
    if driver.find_element_by_link_text("亲，请登录"):
        driver.find_element_by_link_text("亲，请登录").click()
        print("请在15秒内完成扫码")
        time.sleep(15)
        driver.get("https://cart.taobao.com/cart.htm")
    time.sleep(3)
    if driver.find_element_by_id("J_SelectAll1"):
        driver.find_element_by_id("J_SelectAll1").click()
    now = datetime.datetime.now()
    print("登录成功，时间为:", now.strftime("%Y-%m-%d %H:%M:%S"))

def buy(buytime):
    while True:
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print("抢购时间为:"+buytime)
        print("现在时间为:"+now)
        # 对比时间，时间到的话就点击结算
        if now > buytime:
            try:
                if driver.find_element_by_id("J_Go"):
                    driver.find_element_by_id("J_Go").click()
                    driver.find_element_by_link_text("提交订单").click()
            except:
                time.sleep(0.1)
        print(now)
        time.sleep(0.1)

if __name__ == "__main__":
    times = input("请输入抢购时间(例如格式：2018-11-11 00:00:00):")
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(3)
    login()
    buy(times)