import time
from encodings.punycode import adapt
from time import sleep
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver

from qa_python.selenium_examples.seleniumBase import seleniumBase

# print("Test start")
# service = ChromeService(executable_path=ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service)
#
# driver.maximize_window()
# driver.implicitly_wait(10)

base = seleniumBase()
driver = base.selenium_start()

driver.get('https://www.ebay.com/')

advanced_button = driver.find_element(By.LINK_TEXT, "Advanced")
advanced_text = advanced_button.text

if advanced_text == "Advanced":
    print("It's a match")
    advanced_button.click()
    url = driver.current_url
    print(url)
else:
    print("It doesn't match")

driver.close()