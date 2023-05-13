from selenium.webdriver import ActionChains
from pages.base_page import BasePage
from locators.locators import Locators

class DiscountPage(BasePage):

    def click_perfume_link(self):
        self.driver.find_element(*Locators.PERFUME_LINK).click()

    def click_women_perfume_link(self):
        self.driver.find_element(*Locators.WOMEN_PERFUME_LINK).click()

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

    def add_to_cart(self):
        self.driver.find_element(*Locators.ADD_TO_CART_BTN).click()

    def continue_shopping(self):
        self.driver.find_element(*Locators.CONTINUE_SHOPPING_BTN).click()

    def count_cart_items(self):
        cart_items = self.driver.find_element(*Locators.CART_ITEMS)
        count_cart_items = int(cart_items.get_attribute("data-count"))
        return count_cart_items

    def click_on_cart_icon(self):
        cart_icon = self.driver.find_element(*Locators.CART_ICON)
        hover_over_cart_icon = ActionChains(self.driver)
        hover_over_cart_icon.move_to_element(cart_icon).perform()
        cart_icon.click()

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
