from selenium.common import NoSuchElementException
from pages.basket_page import BasketPage
from pages.confirmation_page import ConfirmationPage
from pages.home_page import HomePage
from pages.perfume_woman_page import PerfumeWomenPage
from pages.product_page import ProductPage
from tests.base_test import BaseTest
from locators.locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DiscountTest(BaseTest):

    def test_discount(self):
        home_page_object = HomePage(self.driver)
        perfume_woman_page_object = PerfumeWomenPage(self.driver)
        product_page_object = ProductPage(self.driver)
        basket_page_object = BasketPage(self.driver)
        confirmation_page_object = ConfirmationPage(self.driver)

        wait = WebDriverWait(self.driver, 10)

        # 1. Click on perfume category
        home_page_object.click_perfume_link()
        wait.until(EC.visibility_of_element_located(Locators.WOMEN_PERFUME_LINK))

        # 2. Click on women perfume category
        home_page_object.click_women_perfume_link()
        wait.until(EC.visibility_of_element_located(Locators.FIRST_PRODUCT_ON_THE_LIST))

        # 3. Tick checkbox with 20% discount "Znizka 20%"
        perfume_woman_page_object.tick_20_discount_code()
        wait.until(EC.visibility_of_element_located(Locators.FIRST_PRODUCT_ON_THE_LIST))

        # 4. Verify if all items are eligible for 20% discount
        products = perfume_woman_page_object.verify_search_results()
        for product in products:
            try:
                promo_badge = product.find_element(*Locators.PROMO_BADGE)
            except NoSuchElementException:
                print(f"Product {product.text} is not discounted by 20%")

        # 5. Save discount code -20%
        discount_code = perfume_woman_page_object.get_discount_code()
        print(f"20% dicount code is: {discount_code}.")

        # 6. Click on a first product on the list
        perfume_woman_page_object.click_first_product()

        # 7. Add product to cart
        product_page_object.add_to_cart()
        wait.until(EC.visibility_of_element_located(Locators.CONFIRMATION_ADDED_TO_CART))

        # 8. Go back to main page by clicking continue shopping
        confirmation_page_object.continue_shopping()
        wait.until(EC.element_to_be_clickable(Locators.PERFUME_LINK))

        # 9. Verify if product has been added to cart
        count_cart_items = product_page_object.count_cart_items()
        print(f"Number of products added to cart: {count_cart_items}.")
        assert count_cart_items > 0, "Product was not added to cart"

        # 10. Go to cart page
        product_page_object.click_on_cart_icon()
        wait.until(EC.element_to_be_clickable(Locators.PRODUCT_IN_CART))

        # 11. Verify if item was added to cart in correct amount
        number_of_items = basket_page_object.verify_number_of_items_in_cart()
        print(f"Number of products in the cart: {number_of_items}.")
        self.assertEqual(1, number_of_items)

        # 12. Enter -20% discount code
        basket_page_object.enter_discount_code(discount_code)
        wait.until(EC.visibility_of_element_located(Locators.DISCOUNT_AMOUNT))

        # 13. Verify if discount amount equals 20% price
        price = basket_page_object.get_price()
        discount_amount = basket_page_object.get_discount_amount()
        print(f"Price: {price}, discount applied: {discount_amount}.")
        self.assertAlmostEqual(0.2*price, discount_amount)

        # 14. Verify if total amount visible is correctly discounted
        total_price_visible = basket_page_object.get_total_price_visible()
        print(f"Total price: {total_price_visible}.")
        self.assertAlmostEqual(price-discount_amount, total_price_visible)






