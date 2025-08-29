import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.feature("wikipedia Search")
@allure.story("Search input validation")
def test_search_input(driver):
    with allure.step("open wikipedia homepage"):
     driver.get("https://www.wikipedia.org/")

    with allure.step("wait until the search input is visible"):
       wait = WebDriverWait(driver, 10)
       search_input = wait.until(
          EC.visibility_of_element_located((By.ID, "searchInput"))
      )

       with allure.step("type text into the search input"):
          search_input.send_keys("TestPytest")

       with allure.step("validate that text is entered correctly"):
          assert search_input.get_attribute("value") == "TestPytest","Text not entered correctly"

          print("Text input successful")
          search_input.submit()

          

          
          