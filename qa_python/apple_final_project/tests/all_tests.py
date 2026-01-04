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
        url = self.driver.current_url
        assert "https://www.apple.com/il/search/" in url, "Search page URL is not as expected."

        self.search_page.check_results_found_number_plus_assertion()

        print("Search for a product opened the search results page successfully." )

    def test_count_navigation_buttons(self):
        buttons_count = self.main_page.count_navigation_buttons()
        assert buttons_count == 6, "Unexpected number of navigation buttons."

        print("The main navigation has the expected number of navigation buttons.")

    def test_apple_logo_button_works(self):
        self.main_page.mac_button()
        url = self.driver.current_url
        assert url == "https://www.apple.com/il/mac/", "Mac page URL is not as expected."

        self.mac_page.apple_logo()
        url = self.driver.current_url
        assert url == "https://www.apple.com/il/", "Main page URL is not as expected."

        print("Clicking the Apple logo returned to the main page.")

    def test_text_is_found_in_page(self):
        self.main_page.where_to_buy_button()
        url = self.driver.current_url
        assert url == "https://www.apple.com/il/buy/", "Where to buy page URL is not as expected."

        self.where_to_buy_page.find_a_reseller_button()
        url = self.driver.current_url
        assert url == "https://locate.apple.com/il/en/sales", "Find a reseller page URL is not as expected."

        results_as_text = self.find_a_reseller_page.search_location_and_product(LOCATION)
        assert "sales locations near" in results_as_text, "Unexpected text after searching for product."

        print("The reseller search displayed the expected text.")

    def test_find_a_store_correct_page(self):
        self.main_page.learn_more_button()
        url = self.driver.current_url
        assert url == "https://www.apple.com/il/iphone-17-pro/", "Learn more page URL is not as expected."

        self.learn_more_page.find_a_store_button()
        url = self.driver.current_url
        assert url == "https://www.apple.com/il/buy/?iphone", "Find a store page URL is not as expected."

        print("The Find a Store button opened the correct page.")