from qa_python.apple_final_project.locators import SearchPageLocators


class SearchPage:
    def __init__(self, driver):
        self.driver = driver

    def check_results_found_number(self):
        results = self.driver.find_element(*SearchPageLocators.RESULTS)
        text = results.text.split()

        for i in range(len(text)):
            if text[i] == "results":
                text_as_int = int(text[i - 1])
                print(f"'{text_as_int}' results found.")
                return