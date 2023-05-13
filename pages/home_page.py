from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
from locators.locators import Locators
from pages.nomade_page import NomadePage
from pages.perfume_page import PerfumePage
from pages.perfume_woman_page import PerfumeWomenPage
from test_data.test_data import TestData
from selenium.webdriver.support import expected_conditions as EC


class HomePage(BasePage):
    def click_perfume_link(self):
        self.driver.find_element(*Locators.PERFUME_LINK).click()

    def click_women_perfume_link(self):
        self.driver.find_element(*Locators.WOMEN_PERFUME_LINK).click()
        return PerfumeWomenPage

    def search_item(self):
        search_box = self.driver.find_element(*Locators.SEARCH_BOX_INPUT)
        search_box.send_keys(*TestData.CHOSEN_PERFUME)
        search_box.send_keys(Keys.RETURN)
        return NomadePage

    def click_perfume_img(self):
        perfume_button_quick = self.driver.find_element(*Locators.PERFUME_IMG)
        perfume_button_quick.click()
        return PerfumePage

    def verify_products_removal(self):
        cart_items = self.driver.find_element(*Locators.CART_ICON_ITEMS)
        count_str = cart_items.get_attribute("data-count")
        count = int(count_str)
        return count

    def search_item_cosmetic(self):
        search_box = self.driver.find_element(*Locators.SEARCH_BOX_INPUT)
        search_box.send_keys(*TestData.CHOSEN_COSMETIC)
        search_box.send_keys(Keys.RETURN)

    def choose_body_products(self):
        main_menu_body = self.driver.find_element(*Locators.BODY_CATEGORY)
        ActionChains(self.driver).move_to_element(main_menu_body).perform()

    def click_body_care_products(self):
        wait = WebDriverWait(self.driver, 10)
        body_care_btn = self.driver.find_element(*Locators.BODY_CARE_CATEGORY)
        body_care = wait.until(EC.element_to_be_clickable(Locators.BODY_CARE_CATEGORY))
        body_care.click()

    def _verify_page(self):
        """
        Weryfikacja strony glownej
        """
        pass