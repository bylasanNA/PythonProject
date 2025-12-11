import time
import unittest

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from qa_python.selenium_examples.seleniumBase import seleniumBase


class pytest_swaglabs(unittest.TestCase):

    def setUp(self):
        self.base = seleniumBase()
        self.driver = self.base.selenium_start_with_url("https://www.saucedemo.com/")

    def tearDown(self):
        self.base.selenium_stop()

    def test_login_correct_details(self):
        print("Into test login")
        user = self.driver.find_element(By.ID, "user-name")
        password = self.driver.find_element(By.NAME, "password")
        login_button = self.driver.find_element(By.ID, "login-button")

        user.send_keys("standard_user")
        password.send_keys("secret_sauce")
        login_button.click()
        url = self.driver.current_url
        assert url == "https://www.saucedemo.com/inventory.html", ("URL did not change after login")

    def test_login_incorrect_details(self):
        print("Into test login")
        user = self.driver.find_element(By.ID, "user-name")
        password = self.driver.find_element(By.NAME, "password")
        login_button = self.driver.find_element(By.ID, "login-button")

        user.send_keys("standard_user")
        password.send_keys("secret.sauce")
        login_button.click()
        time.sleep(2) #It’s not recommended to use a large sleep value. The recommended maximum is 5.
        url = self.driver.current_url
        assert url == "https://www.saucedemo.com/", ("URL did not change after login")

    def test_drop_down_example(self):
        print("Into test login")
        user = self.driver.find_element(By.ID, "user-name")
        password = self.driver.find_element(By.NAME, "password")
        login_button = self.driver.find_element(By.ID, "login-button")

        user.send_keys("standard_user")
        password.send_keys("secret.sauce")
        login_button.click()
        sort = self.driver.find_element(By. CLASS_NAME, "product_sort_container")
        sort_as_drop_down = Select(sort)
        sort_as_drop_down.select_by_index(3)
        print("Drop down example")
