from pages.base_page import BasePage
from locators.locators import Locators

class ConfirmationPage(BasePage):
    def continue_shopping(self):
        self.driver.find_element(*Locators.CONTINUE_SHOPPING_BTN).click()

    def go_to_cart(self):
        go_to_cart_btn = self.driver.find_element(*Locators.GO_TO_CART)
        go_to_cart_btn.click()