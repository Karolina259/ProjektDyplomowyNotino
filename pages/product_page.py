from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
from locators.locators import Locators
from pages.confirmation_page import ConfirmationPage
from pages.favourties_all_page import FavouritesAllPage


class ProductPage(BasePage):
    def add_to_cart(self):
        self.driver.find_element(*Locators.ADD_TO_CART_BTN).click()
        return ConfirmationPage

    def count_cart_items(self):
        cart_items = self.driver.find_element(*Locators.CART_ITEMS)
        count_cart_items = int(cart_items.get_attribute("data-count"))
        return count_cart_items

    def click_on_cart_icon(self):
        cart_icon = self.driver.find_element(*Locators.CART_ICON)
        hover_over_cart_icon = ActionChains(self.driver)
        hover_over_cart_icon.move_to_element(cart_icon).perform()
        cart_icon.click()

    def change_number_of_products(self):
        wait = WebDriverWait(self.driver, 10)
        items_count = self.driver.find_element(*Locators.PRODUCT_ITEM_COUNT)
        ActionChains(self.driver).move_to_element(items_count).perform()
        items_count.click()
        self.driver.execute_script("window.scrollBy(0, 530)")
        wait.until(EC.element_to_be_clickable(Locators.PRODUCT_ITEM_COUNT_2))
        items_count_2 = self.driver.find_element(*Locators.PRODUCT_ITEM_COUNT_2)
        items_count_2.click()

    def add_to_favourites(self):
        add_to_favourites = self.driver.find_element(*Locators.ADD_TO_FAVOURITES)
        add_to_favourites.click()

    def verify_favourites_message(self):
        return self.driver.find_element(*Locators.FAVOURITES_MESSAGE).text

    def verify_favourites_message_mini(self):
        favourites_mini_icon = self.driver.find_element(*Locators.FAVOURITES_MINI_ICON)
        countr_str = favourites_mini_icon.get_attribute("data-count")
        count = int(countr_str)
        return count

    def click_all_favourites(self):
        favourites_page = self.driver.find_element(*Locators.FAVOURITES_MINI_ICON)
        favourites_page.click()
        return FavouritesAllPage

