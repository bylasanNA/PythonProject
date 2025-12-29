from selenium.webdriver.common.by import By


class WhereToBuyPage:
    def __init__(self, driver):
        self.driver = driver

    def find_a_reseller_button(self):
        find_a_reseller = self.driver.find_element(By.CLASS_NAME, "icon-copy")
        find_a_reseller.click()

        url = self.driver.current_url
        assert url == "https://locate.apple.com/il/en/sales", "Unexpected URL."