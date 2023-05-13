from pages.base_page import BasePage
from locators.locators import Locators
class BodyProductsPage(BasePage):

    def verify_chosen_category(self):
        category_component_title = (self.driver.find_element(*Locators.CATEGORY_COMPONENT_TITLE).text).lower()
        return category_component_title

    def extend_brands_filter(self):
        brand_filter_expand = self.driver.find_element(*Locators.BRAND_FILTER_EXPAND)
        brand_filter_expand.click()

    def select_brand(self):
        brand_letter_L = self.driver.find_element(*Locators.BRAND_LETTER_L)
        brand_letter_L.click()
        brand_chosen = self.driver.find_element(*Locators.BRAND_LA_ROCHE_POSAY)
        brand_chosen.click()

    def click_sort_button(self):
        sort_button = self.driver.find_element(*Locators.SORT_BTN)
        sort_button.click()

    def click_ascending_sort_option(self):
        price_sort_option = self.driver.find_element(*Locators.ASCENDING_SORT_BTN)
        price_sort_option.click()

    def get_products(self):
        return self.driver.find_elements(*Locators.PRODUCT_ON_THE_LIST)

    def get_products_prices(self):
        return self.driver.find_elements(*Locators.PRICES_SORT)





