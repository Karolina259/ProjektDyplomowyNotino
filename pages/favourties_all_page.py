from pages.base_page import BasePage
from locators.locators import Locators

class FavouritesAllPage(BasePage):

    def get_favourites_page_description(self):
        favourites_page_description = self.driver.find_element(*Locators.FAVOURITES_PAGE_DESCRIPTION)
        return favourites_page_description.text