from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.locators import Locators


class SortPage(BasePage):
    def choose_body_products(self):
        main_menu_body = self.driver.find_element(*Locators.BODY_CATEGORY)
        ActionChains(self.driver).move_to_element(main_menu_body).perform()

    def click_body_care_products(self):
        wait = WebDriverWait(self.driver, 10)
        body_care_btn = self.driver.find_element(*Locators.BODY_CARE_CATEGORY)
        body_care = wait.until(EC.element_to_be_clickable(Locators.BODY_CARE_CATEGORY))
        body_care.click()

    def verify_chosen_category(self):
        category_component_title = (self.driver.find_element(*Locators.CATEGORY_COMPONENT_TITLE).text).lower()
        return category_component_title

    def extend_brands_filter(self):
        brand_filter_expand = self.driver.find_element(*Locators.BRAND_FILTER_EXPAND)
        brand_filter_expand.click()

    def select_brand(self):
        brand_letter_L = self.driver.find_element(*Locators.BRAND_LETTER_L)
        brand_letter_L.click()
        brand_chosen = self.driver.find_element(*Locators.BRAND_LA_ROCHE_POSAY)
        brand_chosen.click()

    def click_sort_button(self):
        sort_button = self.driver.find_element(*Locators.SORT_BTN)
        sort_button.click()

    def click_ascending_sort_option(self):
        price_sort_option = self.driver.find_element(*Locators.ASCENDING_SORT_BTN)
        price_sort_option.click()

    def get_products_prices(self):
        return self.driver.find_elements(*Locators.PRICES)