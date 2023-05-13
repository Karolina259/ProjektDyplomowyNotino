from locators.locators import Locators
from pages.basket_page import BasketPage
from pages.confirmation_page import ConfirmationPage
from pages.home_page import HomePage
from pages.perfume_page import PerfumePage
from pages.product_page import ProductPage
from tests.base_test import BaseTest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartTest(BaseTest):

    def test_cart(self):

        wait = WebDriverWait(self.driver, 10)
        home_page_object = HomePage(self.driver)
        perfume_page_object = PerfumePage(self.driver)
        product_page_object = ProductPage(self.driver)
        basket_page_object = BasketPage(self.driver)
        confirmation_page_object = ConfirmationPage(self.driver)

        # 1. Click on perfume image
        home_page_object.click_perfume_img()

        # 2. Select first element of the list
        perfume_page_object.select_first_product()
        wait.until(EC.element_to_be_clickable(Locators.ADD_TO_CART_BTN))

        # 3. Change number of products from 1 to 2
        product_page_object.change_number_of_products()
        wait.until(EC.visibility_of_element_located(Locators.PRODUCT_ITEM_COUNT))

        # 4. Add 2 products to cart
        product_page_object.add_to_cart()
        wait.until(EC.visibility_of_element_located(Locators.CONFIRMATION_ADDED_TO_CART))

        # 5. Go to cart
        confirmation_page_object.go_to_cart()
        wait.until(EC.element_to_be_clickable(Locators.PRODUCT_IN_CART))

        # 5. Verify if 2 products were added to cart
        number_of_products_verification = basket_page_object.verify_number_of_products()
        assert "2 szt." in number_of_products_verification

        # 6. Remove product from the cart
        basket_page_object.remove_products_from_cart()
        wait.until(EC.invisibility_of_element(Locators.PRODUCT_IN_CART))

        # 7. Verify if products were removed from the cart
        count = home_page_object.verify_products_removal()
        assert count == 0, "Products were not removed from the cart"
        print(f"Number of products in cart after removal: {count}.")