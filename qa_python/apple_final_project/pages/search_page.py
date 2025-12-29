from selenium.webdriver.common.by import By


class SearchPage:
    def __init__(self, driver):
        self.driver = driver

    def check_results_found_number(self):
        results = self.driver.find_element(By.CLASS_NAME, "as-search-results-value")
        text = results.text.split()

        for i in range(len(text)):
            if text[i] == "results":
                text_as_int = int(text[i - 1])
                print(f"'{text_as_int}' results found.")
                return