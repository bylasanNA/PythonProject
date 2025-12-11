import unittest
from selenium.webdriver.common.by import By
from webdriver_manager.core import driver
from qa_python.selenium_examples.seleniumBase import seleniumBase


class ebay_search_advanced(unittest.TestCase):

    def setUp(self):
        self.base = seleniumBase()
        self.driver = self.base.selenium_start_with_url("https://www.ebay.com/")

    def tearDown(self):
        self.base.selenium_stop()

    def test_advanced_button_correct(self):

        advanced_button = self.driver.find_element(By.LINK_TEXT, "Advanced")
        advanced_button.click()

        url = self.driver.current_url
        assert url == "https://www.ebay.com/sch/ebayadvsearch", ("URL is correct")

    def test_search_button_correct(self):

        advanced_button = self.driver.find_element(By.LINK_TEXT, "Advanced")
        advanced_button.click()

        input_search_button = self.driver.find_element(By.CLASS_NAME, "textbox__control")
        input_search_button.click()
        input_search_button.send_keys("Shirt")

        self.driver.find_element(By.CLASS_NAME, "field.adv-keywords__btn-help").click()



