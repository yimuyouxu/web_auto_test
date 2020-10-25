from test1 import lesson7
from test_data import test_data
from selenium import webdriver
driver = webdriver.Chrome()
driver.implicitly_wait(10)
# user_name = test_data.login_data[0]["username"]
# pass_word=test_data.login_data[1]["password"]
# print(user_name,pass_word)
result = lesson7.search_key(test_data.url["url"],
driver=driver,
username=test_data.login_data[0]["username"],
password=test_data.login_data[1]["password"],
s_key=test_data.s_key["s_key"])
if test_data.s_key["s_key"] in result:
    print("搜索结果是正确的")
else:
    print("用例测试不通过！")
