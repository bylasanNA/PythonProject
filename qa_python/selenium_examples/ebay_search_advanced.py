import time
import unittest

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chromium.service import ChromiumService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from socks import PRINTABLE_PROXY_TYPES
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core import driver

from qa_python.selenium_examples.ebay_advanced import url
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
        assert url == "https://www.ebay.com/sch/ebayadvsearch", ("URL is not correct")

    def test_search_button_correct(self):
        advanced_button = self.driver.find_element(By.LINK_TEXT, "Advanced")
        advanced_button.click()

        input_search_button = self.driver.find_element(By.CLASS_NAME, "textbox__control")
        input_search_button.click()
        input_search_button.send_keys("Shirt")
        input_search_button.send_keys(Keys.ENTER)

    def test_keyword_option(self):
        advanced_button = self.driver.find_element(By.LINK_TEXT, "Advanced")
        advanced_button.click()

        keyword_option = self.driver.find_element(By.NAME, "_in_kw")
        keyword_option_as_dropdown = Select(keyword_option)
        keyword_option_as_dropdown.select_by_index(2)

        input_search_button = self.driver.find_element(By.CLASS_NAME, "textbox__control")
        input_search_button.click()
        input_search_button.send_keys("Shirt")
        input_search_button.send_keys(Keys.ENTER)

        url = self.driver.current_url
        assert "https://www.ebay.com" in url, "ebay did not found at URL after search"

    def test_checkbox_radio_correct(self):
        advanced_button = self.driver.find_element(By.LINK_TEXT, "Advanced")
        advanced_button.click()

        check_box = self.driver.find_element(By.NAME, "LH_TitleDesc")
        check_box.click()

        radio = self.driver.find_element(By.NAME, "s0-1-20-6[3]")
        radio.click()

    def test_checkbox_example(self):
        adv = self.driver.find_element(By.PARTIAL_LINK_TEXT, "Advanced")
        adv.click()

        time.sleep(2)

        desc = self.driver.find_element(By.NAME, "LH_TitleDesc")
        is_selected = desc.is_selected()

        if is_selected == False:
            desc.click()
        after = desc.is_selected()
        assert after == True, "Click did not function as expected"

    def test_checkbox_example(self):

        adv = self.driver.find_element(By.PARTIAL_LINK_TEXT, "Advanced")
        adv.click()

        time.sleep(2)
        desc = self.driver.find_element(By.NAME, "LH_TitleDesc")