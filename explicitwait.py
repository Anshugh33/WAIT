from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome()
driver.get("https://www.wikipedia.org/")

#wait until the search input is visible
wait=WebDriverWait(driver, 10)
search_input = wait.until(
    EC.visibility_of_element_located((By.ID,"searchinput"))

)

search_input.send_keys("test")

#validation immediately
assert search_input.get_attribute("value") == "Test", "Text not entered correctly"

print("validation passed: Text is in the input box")

driver.quit()