from selenium.webdriver.common.by import By


class FindAResellerPage:
    def __init__(self, driver):
        self.driver = driver

    def search_location_and_product(self, location):
        enter_location = self.driver.find_element(By.ID, "sales-address")
        enter_location.click()
        enter_location.send_keys(location)

        all_products = self.driver.find_element(By.CLASS_NAME, "svg-icon.selector-icon")
        all_products.click()

        go_button = self.driver.find_element(By.CSS_SELECTOR, 'button[class="button button-elevated button-block"]')
        go_button.click()

        sales_results = self.driver.find_element(By.CLASS_NAME, "search-text")
        text = sales_results.text

        assert "sales locations near" in text, "Unexpected text."
        print(text)