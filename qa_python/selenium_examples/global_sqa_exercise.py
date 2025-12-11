from selenium.webdriver.common.by import By

from qa_python.selenium_examples.seleniumBase import seleniumBase

base = seleniumBase()

driver = base.selenium_start_with_url("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")

elements = driver.find_elements(By.CLASS_NAME, "btn.btn-primary.btn-lg")
login = elements[1]
login.click()

base.selenium_stop()