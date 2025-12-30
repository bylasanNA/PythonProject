from qa_python.apple_final_project.locators import SearchPageLocators


class SearchPage:
    def __init__(self, driver):
        self.driver = driver

    def check_results_found_number_plus_assertion(self):
        results = self.driver.find_element(*SearchPageLocators.RESULTS)
        results_as_text = results.text.split()

        for i in range(len(results_as_text)):
            if results_as_text[i] == "results":
                text_as_int = int(results_as_text[i - 1])
                print(f"'{text_as_int}' results found.")
                assert text_as_int >= 0, "Number of results is invalid."
                return