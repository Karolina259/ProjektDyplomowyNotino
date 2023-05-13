from selenium.webdriver import Keys
from pages.base_page import BasePage
from test_data.test_data import TestData
from locators.locators import Locators

class RefreshPage(BasePage):
    def search_item(self):
        search_box = self.driver.find_element(*Locators.SEARCH_BOX_INPUT)
        search_box.send_keys(*TestData.CHOSEN_PERFUME)
        search_box.send_keys(Keys.RETURN)

    def search_results(self):
        return self.driver.find_elements(*Locators.SEARCH_RESULTS)

    def filter_price(self):
        price_filter = self.driver.find_element(*Locators.PRICE_FILTER)
        price_filter.send_keys(*TestData.CHOSEN_MAX_PRICE)
        body = self.driver.find_element(*Locators.BODY)
        body.click()

    def find_prices(self):
        return self.driver.find_elements(*Locators.PRICES)

    def get_search_results_number(self):
        product_count = self.driver.find_element(*Locators.PRODUCT_COUNT).text
        product_count_before_refresh = int(product_count.split()[-1])
        return product_count_before_refresh

    def search_results_after_refresh(self):
        return len(self.driver.find_elements(*Locators.SEARCH_RESULTS))

    def verify_search_results_after_refresh(self):
        product_count_2 = self.driver.find_element(*Locators.PRODUCT_COUNT).text
        product_count_after_refresh = int(product_count_2.split()[-1])
        return product_count_after_refresh
