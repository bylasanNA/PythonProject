import time

from selenium.webdriver import Keys

from qa_python.apple_final_project.locators import MainPageLocators


class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def search_for_product(self, product):
        search_button = self.driver.find_element(*MainPageLocators.SEARCH_BUTTON)
        search_button.click()

        search_for_a_product = self.driver.find_element(*MainPageLocators.SEARCH_FOR_PRODUCT)
        search_for_a_product.send_keys(product)
        time.sleep(1)
        search_for_a_product.send_keys(Keys.ENTER)

    def check_navigation_buttons(self):
        navigation_buttons = self.driver.find_elements(*MainPageLocators.NAVIGATION_BUTTONS)
        buttons_count = len(navigation_buttons)
        print(f"There are {buttons_count} navigation navigation_buttons.")
        return buttons_count

    def mac_button(self):
        mac_button = self.driver.find_element(*MainPageLocators.MAC_BUTTON)
        mac_button.click()

    def where_to_buy_button(self):
        where_to_buy = self.driver.find_element(*MainPageLocators.WHERE_TO_BUY)
        where_to_buy.click()

        url = self.driver.current_url
        assert url == "https://www.apple.com/il/buy/", "Unexpected URL."

    def learn_more_button(self):
        learn_more = self.driver.find_element(*MainPageLocators.LEARN_MORE)
        learn_more.click()