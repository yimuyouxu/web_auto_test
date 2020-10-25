import  time
def login_page(username,password,driver):
    driver.find_element_by_id("username").send_keys(username)
    driver.find_element_by_id("password").send_keys(password)
    driver.find_element_by_id("btnSubmit").click()
def open_url(url,driver):
    driver.get(url)  # 打开一个网址
    driver.maximize_window()

def search_key(url,driver,username,password,s_key):
    open_url(url,driver)
    login_page(username,password,driver)
    driver.find_element_by_xpath('//span[text()="零售出库"]').click()
    id_1 = driver.find_element_by_xpath('//div[text()="零售出库"]/..').get_attribute("id")
    id_2 = id_1 + "-frame"
    print(id_2)
    driver.switch_to.frame(driver.find_element_by_xpath('//iframe[@id="{}"]'.format(id_2)))
    driver.find_element_by_id("searchNumber").send_keys(s_key)
    driver.find_element_by_id("searchBtn").click()
    time.sleep(1)
    num = driver.find_element_by_xpath('//tr[@id="datagrid-row-r1-2-0"]//td[@field="number"]/div').text
    return num