from qa_python.apple_final_project.locators import LearnMorePageLocators


class LearnMorePage:
    def __init__(self, driver):
        self.driver = driver

    def find_a_store_button(self):
        find_a_store = self.driver.find_element(*LearnMorePageLocators.FIND_A_STORE)
        find_a_store.click()