from locators.locators import Locators
from pages.body_products_page import BodyProductsPage
from pages.home_page import HomePage
from tests.base_test import BaseTest
from test_data.test_data import TestData
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

search_query = TestData.CATEGORY_COMPONENT

class SortTest(BaseTest):

    def test_sort(self):

        home_page_object = HomePage(self.driver)
        body_products_page_object = BodyProductsPage(self.driver)

        wait = WebDriverWait(self.driver, 10)

        # 1. Choose body products in menu wrapper
        home_page_object.choose_body_products()

        # 2. Choose body care button
        home_page_object.click_body_care_products()

        # 3. Verify if given results are in line with chosen category
        category_component_title = body_products_page_object.verify_chosen_category()
        print(f"Category component title: {category_component_title}, search query: {search_query}.")
        assert search_query in category_component_title, f"No results for category: {search_query}"

        # 4. Extend filter with brands choice
        body_products_page_object.extend_brands_filter()

        # 5. Select brand La Roche-Posay
        body_products_page_object.select_brand()

        # 6. Click on sort option button
        body_products_page_object.click_sort_button()

        # 7. Click on ascending sorting option: "Cena - rosnąco"
        body_products_page_object.click_ascending_sort_option()
        wait.until(EC.element_to_be_clickable(Locators.FIRST_PRODUCT_ON_THE_LIST))

        # 8. Verify if products are sorted in ascending order
        wait.until(EC.visibility_of_element_located(Locators.PRICES_SORT))
        prices = body_products_page_object.get_products_prices()
        prices_list = []

        for price in prices:
            price_str = price.text
            price_dot = price_str.replace(",", ".")
            price_dot_number = float(price_dot)
            prices_list.append(price_dot_number)

        print(f"Product prices are: {prices_list}.")

        if prices_list == sorted(prices_list):
            print("Products are sorted in ascending order.")
        else:
            print("Products are not sorted in ascending order.")


