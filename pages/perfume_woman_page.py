from pages.base_page import BasePage
from pages.product_page import ProductPage
from locators.locators import Locators
class PerfumeWomenPage(BasePage):
    def tick_20_discount_code(self):
        self.driver.find_element(*Locators.DISCOUNT_20_CHECKBOX).click()

    def verify_search_results(self):
        products = self.driver.find_elements(*Locators.FIRST_PRODUCT_ON_THE_LIST)
        return products

    def get_discount_code(self):
        discount_code = self.driver.find_element(*Locators.DISCOUNT_CODE)
        discount_code_text = discount_code.text
        print(discount_code_text)
        return discount_code_text

    def click_first_product(self):
        self.driver.find_element(*Locators.FIRST_PRODUCT_ON_THE_LIST).click()
        return ProductPage

