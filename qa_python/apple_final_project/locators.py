from selenium.webdriver.common.by import By


class MainPageLocators:
    SEARCH_BUTTON = (By.ID, "globalnav-menubutton-link-search")
    SEARCH_FOR_PRODUCT = (By.CLASS_NAME, "globalnav-searchfield-input")

    NAVIGATION_BUTTONS = (By.CLASS_NAME, "globalnav-submenu-trigger-group")

    MAC_BUTTON = (By.CLASS_NAME, "globalnav-link-text-container")

    WHERE_TO_BUY = (By.CLASS_NAME, "globalnav-link.globalnav-submenu-trigger-link.globalnav-link-where-to-buy")

    LEARN_MORE = (By.CLASS_NAME, "button.button-elevated.button-primary")

class SearchPageLocators:
    RESULTS = (By.CLASS_NAME, "as-search-results-value")

class MacPageLocators:
    APPLE_LOGO = (By.CLASS_NAME, "globalnav-link.globalnav-link-apple")

class WhereToBuyPageLocators:
    FIND_A_RESELLER = (By.CLASS_NAME, "icon-copy")

class FindAResellerPageLocators:
    LOCATION_INPUT = (By.ID, "sales-address")
    ALL_PRODUCTS = (By.CLASS_NAME, "svg-icon.selector-icon")
    GO_BUTTON = (By.CSS_SELECTOR, 'button[class="button button-elevated button-block"]')
    SALES_RESULTS = (By.CLASS_NAME, "search-text")

class LearnMorePageLocators:
    FIND_A_STORE = (By.CLASS_NAME, "marquee-ctas-link.button")