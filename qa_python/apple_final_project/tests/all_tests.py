import unittest

from qa_python.apple_final_project.globals import BASE_URL, PRODUCT, LOCATION
from qa_python.apple_final_project.pages.find_a_reseller_page import FindAResellerPage
from qa_python.apple_final_project.pages.learn_more_page import LearnMorePage
from qa_python.apple_final_project.pages.mac_page import MacPage
from qa_python.apple_final_project.pages.main_page import MainPage
from qa_python.apple_final_project.pages.search_page import SearchPage
from qa_python.apple_final_project.pages.where_to_buy_page import WhereToBuyPage
from qa_python.apple_final_project.tests.selenium_base_apple import SeleniumBaseApple


class AllTests(unittest.TestCase):
    def setUp(self):
        self.base = SeleniumBaseApple()
        self.driver = self.base.selenium_start_with_url(BASE_URL)
        self.main_page = MainPage(self.driver)
        self.search_page = SearchPage(self.driver)
        self.mac_page = MacPage(self.driver)
        self.where_to_buy_page = WhereToBuyPage(self.driver)
        self.find_a_reseller_page = FindAResellerPage(self.driver)
        self.learn_more_page = LearnMorePage(self.driver)

    def tearDown(self):
        self.base.selenium_stop()

    def test_search_for_a_product(self):
        self.main_page.search_for_product(PRODUCT)
        self.search_page.check_results_found_number()

    def test_main_buttons_exist(self):
        self.main_page.check_navigation_buttons()

    def test_apple_logo(self):
        self.main_page.mac_button()
        self.mac_page.apple_logo()

    def test_text_is_found_in_page(self):
        self.main_page.where_to_buy_button()
        self.where_to_buy_page.find_a_reseller_button()
        self.find_a_reseller_page.search_location_and_product(LOCATION)

    def test_find_a_store_correct_page(self):
        self.main_page.learn_more_button()
        self.learn_more_page.find_a_store_button()