import time
from time import sleep
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver

print("Test start")
service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.maximize_window()
driver.implicitly_wait(10)

driver.get('https://www.calculator.net/')
age_link = driver.find_element(By.LINK_TEXT, "Age Calculator")
age_link.click()

driver.find_element(By.PARTIAL_LINK_TEXT, "FITNESS").click()

url = driver.current_url
print(url)

if (url == 'https://www.calculator.net/fitness-and-health-calculator.html'):
    print("Test is OK - URL is as expected")

else:
    print("Test failed - URL is not as expected")


driver.close()