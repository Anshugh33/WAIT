from selenium import webdriver

driver = webdriver.Chrome()

#implicit wait applies globally
driver.implicitly_wait(10) #wait up to 10 seconds for elements

driver.get("https://www.google.com")

#wait automatically if element is not yet loaded
search_box = driver.find_element("name","q")
search_box.send_keys("selenium Python")

#submit the search
search_box.submit()

driver.quit()