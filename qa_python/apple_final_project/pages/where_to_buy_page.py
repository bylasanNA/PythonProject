from qa_python.apple_final_project.locators import WhereToBuyPageLocators


class WhereToBuyPage:
    def __init__(self, driver):
        self.driver = driver

    def find_a_reseller_button(self):
        find_a_reseller = self.driver.find_element(*WhereToBuyPageLocators.FIND_A_RESELLER)
        find_a_reseller.click()