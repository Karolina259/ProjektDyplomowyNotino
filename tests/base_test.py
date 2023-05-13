from pages.basket_page import BasketPage
from pages.body_products_page import BodyProductsPage
from pages.cart_page import CartPage
from pages.confirmation_page import ConfirmationPage
from pages.cosmetic_page import CosmeticPage
from pages.discount_page import DiscountPage
import unittest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators.locators import Locators
from pages.favourites_page import FavouritesPage
from pages.favourties_all_page import FavouritesAllPage
from pages.home_page import HomePage
from pages.nomade_page import NomadePage
from pages.perfume_page import PerfumePage
from pages.perfume_woman_page import PerfumeWomenPage
from pages.product_page import ProductPage
from pages.refresh_page import RefreshPage
from pages.sort_page import SortPage


class BaseTest(unittest.TestCase):

    def setUp(self):
        #Open browser
        self.driver = webdriver.Chrome()
        #Maximize window
        self.driver.maximize_window()
        #Go to main page
        self.driver.get("https://www.notino.pl/")
        #Create instances of pages
        self.basket_page_object = BasketPage(self.driver)
        self.body_products_page_object = BodyProductsPage(self.driver)
        self.cart_page_object = CartPage(self.driver)
        self.confirmation_page_object = ConfirmationPage(self.driver)
        self.cosmetic_page_object = CosmeticPage(self.driver)
        self.discount_page_object =DiscountPage(self.driver)
        self.favourites_page_object =FavouritesPage(self.driver)
        self.favourites_all_page_object =FavouritesAllPage(self.driver)
        self.home_page_object =HomePage(self.driver)
        self.nomade_page_object =NomadePage(self.driver)
        self.perfume_page_object =PerfumePage(self.driver)
        self.perfume_woman_page_object =PerfumeWomenPage(self.driver)
        self.product_page_object =ProductPage(self.driver)
        self.refresh_page_object =RefreshPage(self.driver)
        self.sort_page_object =SortPage(self.driver)

        self.driver.find_element(*Locators.COOKIES_BTN).click()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(Locators.MAIN_MENU))

    def tearDown(self):
        #Quit the browser
        self.driver.quit()


