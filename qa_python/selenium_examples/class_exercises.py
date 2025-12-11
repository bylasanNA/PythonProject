from selenium.webdriver.common.by import By

from qa_python.selenium_examples.seleniumBase import seleniumBase

base = seleniumBase()

driver = base.selenium_start_with_url("https://www.saucedemo.com/")

elements = driver.find_elements(By.CLASS_NAME, "input_error.form_input")
user = elements[0]
user.send_keys("standard_user")
password = elements[1]
password.send_keys("secret_sauce")
login_button = driver.find_element(By.ID, "login-button")
login_button.click()

base.selenium_stop()
