import time
from time import sleep
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver

from qa_python.selenium_examples.my_first_test import user

print("Test start")
service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://demo.guru99.com/test/newtours/index.php")

user=driver.find_element(By.NAME, "userName")
user.click()
user.send_keys("Eli")

password = driver.find_element(By.NAME, "password")
password.click()
password.send_keys("PinkFluffyUnicorn")

driver.close()