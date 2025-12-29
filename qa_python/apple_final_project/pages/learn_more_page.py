from selenium.webdriver.common.by import By


class LearnMorePage:
    def __init__(self, driver):
        self.driver = driver

    def find_a_store_button(self):
        find_a_store = self.driver.find_element(By.CLASS_NAME, "marquee-ctas-link.button")
        find_a_store.click()

        url = self.driver.current_url
        assert url == "https://www.apple.com/il/buy/?iphone", "Unexpected URL."