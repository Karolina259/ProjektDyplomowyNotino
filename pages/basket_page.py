from pages.base_page import BasePage
from locators.locators import Locators
from pages.home_page import HomePage


class BasketPage(BasePage):

    def verify_number_of_items_in_cart (self):
        number_of_items = int((self.driver.find_element(*Locators.NUMBER_OF_ITEMS_IN_CART)).text[0])
        return number_of_items

    def enter_discount_code(self, discount_code):
        discount_code_input_box = self.driver.find_element(*Locators.DISCOUNT_CODE_INPUT)
        discount_code_input_box.send_keys(discount_code)
        self.driver.find_element(*Locators.OK_BTN).click()

    def get_price(self):
        price = self.driver.find_element(*Locators.PRICE_AMOUNT).text[:-3]
        price_dot = (price.replace(",", "."))
        price_dot_float = float(price_dot)
        return price_dot_float

    def get_discount_amount(self):
        discount_amount = self.driver.find_element(*Locators.DISCOUNT_AMOUNT).text[1:-3]
        discount_amount_with_dot = discount_amount.replace(",", ".")
        discount_amount_with_dot_float = float(discount_amount_with_dot)
        return discount_amount_with_dot_float

    def get_total_price_visible(self):
        total_price_visible = self.driver.find_element(*Locators.TOTAL_PRICE_VISIBLE).text
        total_price_visible_dot = total_price_visible.replace(",", ".")
        total_price_visible_dot_float = float(total_price_visible_dot)
        return total_price_visible_dot_float

    def verify_number_of_products(self):
        return self.driver.find_element(*Locators.NUMBER_OF_ITEMS_VERIFICATION).text

    def remove_products_from_cart(self):
        remove_btn = self.driver.find_element(*Locators.REMOVE_PRODUCTS_FROM_CART)
        remove_btn.click()
        return HomePage
