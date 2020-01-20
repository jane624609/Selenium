from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://displaynote.com/broadcast/')
element = driver.find_element_by_id('broadcastId')

element.send_keys("111111")
element_icon = driver.find_element_by_id('viewer')
element_icon.click()
#send_keys("hello world")