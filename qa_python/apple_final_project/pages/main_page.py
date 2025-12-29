from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def search_for_product(self, product):
        search_button = self.driver.find_element(By.ID, "globalnav-menubutton-link-search")
        search_button.click()

        search_for_a_product = self.driver.find_element(By.CLASS_NAME, "globalnav-searchfield-input")
        search_for_a_product.send_keys(product)
        search_for_a_product.send_keys(Keys.ENTER)

        url = self.driver.current_url
        assert "https://www.apple.com/il/search/" in url, "Unexpected URL."

    def check_navigation_buttons(self):
        buttons = self.driver.find_elements(By.CLASS_NAME, "globalnav-submenu-trigger-group")
        buttons_count = len(buttons)
        print(f"There are {buttons_count} navigation buttons.")

        assert buttons_count == 6, "Unexpected number of navigation buttons."

    def mac_button(self):
        mac_button = self.driver.find_element(By.CLASS_NAME, "globalnav-link-text-container")
        mac_button.click()

        url = self.driver.current_url
        assert url == "https://www.apple.com/il/mac/", "Unexpected URL."

    def where_to_buy_button(self):
        where_to_buy = self.driver.find_element(By.CLASS_NAME, "globalnav-link.globalnav-submenu-trigger-link.globalnav-link-where-to-buy")
        where_to_buy.click()

        url = self.driver.current_url
        assert url == "https://www.apple.com/il/buy/", "Unexpected URL."

    def learn_more_button(self):
        learn_more = self.driver.find_element(By.CLASS_NAME, "button.button-elevated.button-primary")
        learn_more.click()

        url = self.driver.current_url
        assert url == "https://www.apple.com/il/iphone-17-pro/", "Unexpected URL."