from qa_python.apple_final_project.locators import FindAResellerPageLocators


class FindAResellerPage:
    def __init__(self, driver):
        self.driver = driver

    def search_location_and_product(self, location):
        location_input = self.driver.find_element(*FindAResellerPageLocators.LOCATION_INPUT)
        location_input.click()
        location_input.send_keys(location)

        all_products = self.driver.find_element(*FindAResellerPageLocators.ALL_PRODUCTS)
        all_products.click()

        go_button = self.driver.find_element(*FindAResellerPageLocators.GO_BUTTON)
        go_button.click()

        sales_results = self.driver.find_element(*FindAResellerPageLocators.SALES_RESULTS)
        results_as_text = sales_results.text
        print(f"Text found after searching is: {results_as_text}")
        return results_as_text

