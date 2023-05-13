from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.locators import Locators

class CartPage(BasePage):

    def click_perfume_img(self):
        perfume_button_quick = self.driver.find_element(*Locators.PERFUME_IMG)
        perfume_button_quick.click()

    def select_first_product(self):
        first_product = self.driver.find_element(*Locators.FIRST_PRODUCT_ON_THE_LIST)
        first_product.click()

    def change_number_of_products(self):
        wait = WebDriverWait(self.driver, 10)
        items_count = self.driver.find_element(*Locators.PRODUCT_ITEM_COUNT)
        ActionChains(self.driver).move_to_element(items_count).perform()
        items_count.click()
        self.driver.execute_script("window.scrollBy(0, 500)")
        wait.until(EC.element_to_be_clickable(Locators.PRODUCT_ITEM_COUNT_3))
        items_count_3 = self.driver.find_element(*Locators.PRODUCT_ITEM_COUNT_3)
        items_count_3.click()

    def add_to_cart(self):
        add_to_cart_btn = self.driver.find_element(*Locators.ADD_TO_CART)
        add_to_cart_btn.click()

    def go_to_cart(self):
        go_to_cart_btn = self.driver.find_element(*Locators.GO_TO_CART)
        go_to_cart_btn.click()

    def verify_number_of_products(self):
        return self.driver.find_element(*Locators.NUMBER_OF_ITEMS_VERIFICATION).text

    def remove_products_from_cart(self):
        remove_btn = self.driver.find_element(*Locators.REMOVE_PRODUCTS_FROM_CART)
        remove_btn.click()

    def verify_products_removal(self):
        cart_items = self.driver.find_element(*Locators.CART_ICON_ITEMS)
        count_str = cart_items.get_attribute("data-count")
        count = int(count_str)
        return count