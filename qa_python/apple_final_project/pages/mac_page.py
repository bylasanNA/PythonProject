from qa_python.apple_final_project.locators import MacPageLocators


class MacPage:
    def __init__(self, driver):
        self.driver = driver

    def apple_logo(self):
        apple_logo = self.driver.find_element(*MacPageLocators.APPLE_LOGO)
        apple_logo.click()