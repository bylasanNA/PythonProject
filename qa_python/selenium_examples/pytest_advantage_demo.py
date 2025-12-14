import time
import unittest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from qa_python.selenium_examples.seleniumBase import seleniumBase


class advantage_demo(unittest.TestCase):

    def setUp(self):
        self.base = seleniumBase()
        self.driver = self.base.selenium_start_with_url("https://advantageonlineshopping.com/#/")

    def tearDown(self):
        self.base.selenium_stop()

    def test_drop_down_example(self):
        print("Start test for drop down example")
        time.sleep(5)
        contact_us_button = self.driver.find_element(By.PARTIAL_LINK_TEXT, "CONTACT")
        contact_us_button.click()

        category = self.driver.find_element(By.NAME, "categoryListboxContactUs")
        category_as_drop_down = Select(category)
        category_as_drop_down.select_by_index(2)
        category_as_drop_down.select_by_visible_text("Mice")

        product = self.driver.find_element(By.NAME, "productListboxContactUs")
        product_as_drop_down = Select(product)
        product_as_drop_down.select_by_visible_text("HP Z3200 Wireless Mouse")

        email = self.driver.find_element(By.NAME, "emailContactUs")
        email.send_keys("bylasan@gmail.com")

        subject = self.driver.find_element(By.NAME, "subjectTextareaContactUs")
        subject.send_keys("nothing")

        send = self.driver.find_element(By.ID, "send_btn")
        is_displayed = send.is_displayed()
        assert is_displayed == True, "Send button is not displayed as expected"





