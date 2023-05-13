from selenium.webdriver import Keys
from test_data.test_data import TestData
from pages.base_page import BasePage
from locators.locators import Locators


class FavouritesPage(BasePage):

    def search_item(self):
        search_box = self.driver.find_element(*Locators.SEARCH_BOX_INPUT)
        search_box.send_keys(*TestData.CHOSEN_COSMETIC)
        search_box.send_keys(Keys.RETURN)

    def click_first_product(self):
        first_product = self.driver.find_element(*Locators.FIRST_PRODUCT_ON_THE_LIST)
        first_product.click()

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

    def get_favourites_page_description(self):
        favourites_page_description = self.driver.find_element(*Locators.FAVOURITES_PAGE_DESCRIPTION)
        return favourites_page_description.text