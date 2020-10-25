# def add_fun(num):
#     sum_1 = 0
#     for i in range(num):
#         sum_1 += i
#     print(sum_1)
# add_fun(6)




from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("http://erp.lemfix.com")   #打开一个网址
driver.maximize_window()
# time.sleep(2)     #是一种等待，单位默认为秒
# driver.get("http://erp.lemfix.com")
# time.sleep(2)
# driver.back()
# time.sleep(2)
# driver.forward()
# time.sleep(2)
# driver.refresh()
# driver.quit()  #关闭驱动  session（会话）关闭
# driver.close()   #关闭当前窗口   不会退出session(会话)
# driver.find_element_by_id("username").send_keys("test123")
# driver.find_element_by_id("password").send_keys("123456")
# driver.find_element_by_id("btnSubmit").click()
id_1 = driver.find_element_by_xpath('//li[contains(@id,"tabpanel")]').get_attribute("id")
id_2 = id_1 + "-frame"
print()