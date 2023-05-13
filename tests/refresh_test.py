from locators.locators import Locators
from pages.home_page import HomePage
from pages.nomade_page import NomadePage
from tests.base_test import BaseTest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RefreshTest(BaseTest):

    def test_refresh_page(self):

        home_page_object = HomePage(self.driver)
        nomade_page_object = NomadePage(self.driver)

        wait = WebDriverWait(self.driver, 10)

        # 1. Search given phrase
        home_page_object.search_item()
        wait.until(EC.visibility_of_element_located(Locators.FIRST_PRODUCT_ON_THE_LIST))

        # 2. Verify if search results are visible
        results = nomade_page_object.search_results()
        assert len(results) > 0, "No products found matching search keys"

        # 3. Filter prices up to 300 PLN
        nomade_page_object.filter_price()
        wait.until(EC.visibility_of_element_located(Locators.FIRST_PRODUCT_ON_THE_LIST))

        # 4. Find elements with product prices
        prices = nomade_page_object.find_prices()

        # 5. Check if every element is less or equal to 300 PLN
        for price in prices:
            price_str = price.text
            price_dot = price_str.replace(",", ".").replace(" zł", "")
            price_dot_number = float(price_dot.split('\n')[0])
            price_dot_float = float(price_dot_number)
            assert price_dot_float <= 300.0, f"Product with price {price_str} zł doesn't meet price requirement"

        # 6. Find number of search result before page refresh
        product_count_before_refresh = nomade_page_object.get_search_results_number()
        print(f"Number of products before page refresh: {product_count_before_refresh}")

        # 7. Refresh the page
        self.driver.refresh()
        wait.until(EC.visibility_of_element_located(Locators.FIRST_PRODUCT_ON_THE_LIST))

        # 8. Verify if search results are visible after page refresh
        num_results_after_refresh = nomade_page_object.search_results_after_refresh()
        assert num_results_after_refresh > 0, "No products meeting search criteria were found after page refresh"

        # 9. Assure that search results' number didn't change after page refresh
        product_count_after_refresh = nomade_page_object.verify_search_results_after_refresh()
        print(f"Number of products after page refresh: {product_count_after_refresh}")

        if product_count_after_refresh == product_count_before_refresh:
            print("Search results' number didn't change after page refresh")
        else:
            assert product_count_after_refresh == product_count_before_refresh, "Search results' number changed after page refresh"
