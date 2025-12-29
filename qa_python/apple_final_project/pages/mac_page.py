from selenium.webdriver.common.by import By


class MacPage:
    def __init__(self, driver):
        self.driver = driver

    def apple_logo(self):
        apple_logo = self.driver.find_element(By.CLASS_NAME, "globalnav-link.globalnav-link-apple")
        apple_logo.click()

        url = self.driver.current_url
        assert url == "https://www.apple.com/il/", "Unexpected URL."