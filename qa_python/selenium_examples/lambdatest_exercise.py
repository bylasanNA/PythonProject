from selenium.webdriver.common.by import By

from qa_python.selenium_examples.seleniumBase import seleniumBase

base = seleniumBase()

driver = base.selenium_start_with_url("https://ecommerce-playground.lambdatest.io/index.php?route=common/home")

windows = driver.find_element(By.CLASS_NAME, "figure-img.img-fluid.lazy-load")
windows.click()

prices = driver.find_elements(By.CLASS_NAME, "price-new")
for price in prices:
    text_by_loop = price.text
    print(text_by_loop)

base.selenium_stop()
