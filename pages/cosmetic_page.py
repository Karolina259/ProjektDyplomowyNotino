from pages.base_page import BasePage
from locators.locators import Locators
from pages.product_page import ProductPage


class CosmeticPage(BasePage):

    def click_first_product(self):
        first_product = self.driver.find_element(*Locators.FIRST_PRODUCT_ON_THE_LIST)
        first_product.click()
        return ProductPage

