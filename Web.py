#開網頁
from selenium import webdriver
#使用chrome的webdriver
browser = webdriver.Chrome()
#開啟google首頁
browser.get('http://google.com/')


#開網頁並搜尋
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.google.com")
#找到輸入框
element = driver.find_element_by_name("q");
#輸入內容
element.send_keys("hello world");
#提交表單
element.submit();



#import time
#如果需要執行完自動關閉，就要加上下面這一行
#time.sleep(10)
#browser.close()