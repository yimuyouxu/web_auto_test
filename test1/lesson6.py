from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.implicitly_wait(50)    #隐式等待默认等待10秒  即是最多等待10秒，若果元素提前出现了，就不继续等待了
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
driver.find_element_by_id("username").send_keys("test123")
driver.find_element_by_id("password").send_keys("123456")
driver.find_element_by_id("btnSubmit").click()
# driver.find_element_by_xpath('//input[@id="username"]').send_keys("test123")
page_text = driver.find_element_by_xpath('//div[@class="login-logo"]//b').text  #找到这个元素的位置之后获取它的文本信息并赋值给一个变量
if page_text == "柠檬ERP":
    print("这个页面的标题是：{}".format(page_text))
else:
    print("这条测试用例不通过")
page_title = driver.title   #获取页面标题
print("这个页面的标题是是{}".format(page_title))
# time.sleep(5)
# login_user = driver.find_element_by_xpath('//p[text()="测试用户"]').text
login_user = driver.find_element_by_xpath('//div[@class="pull-left info"]//p').text  #获取到登录用户名
# login_user = driver.find_element_by_xpath('//p[contains(text(),"测试")]').text
if login_user == "测试用户":
    print("这个登录的用户是：{}".format(login_user))
else:
    print("这条测试用例不通过")
driver.find_element_by_xpath('//span[text()="零售出库"]').click()
# id_1 = driver.find_element_by_xpath('//li[2][contains(@id,"tabpanel")]').get_attribute("id")
# id_1 = driver.find_element_by_xpath('//div[text()="零售出库"]/..').get_attribute("id")
# id_2 = id_1 + "-frame"
# print(id_2)
# driver.switch_to.frame(driver.find_element_by_xpath('//iframe[@id="{}"]'.format(id_2)))
driver.switch_to.frame(1)
driver.find_element_by_id("searchNumber").send_keys("314")
driver.find_element_by_id("searchBtn").click()
# num = driver.find_element_by_xpath('//div[text()="LSCK00000000314"]').text    ???
time.sleep(1)
num = driver.find_element_by_xpath('//tr[@id="datagrid-row-r1-2-0"]//td[@field="number"]/div').text
if "314" in num:
    print("搜索结果是正确的")
else:
    print("用例测试不通过！")