from locators.locators import Locators
from pages.cosmetic_page import CosmeticPage
from pages.favourties_all_page import FavouritesAllPage
from pages.home_page import HomePage
from pages.product_page import ProductPage
from tests.base_test import BaseTest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FavouritesTest(BaseTest):

    def test_filter(self):

        home_page_object = HomePage(self.driver)
        favourites_all_page_object = FavouritesAllPage(self.driver)
        product_page_object = ProductPage(self.driver)
        cosmetic_page_object = CosmeticPage(self.driver)

        wait = WebDriverWait(self.driver, 10)

        # 1. Search for product face cream: "krem do twarzy" in main menu
        home_page_object.search_item_cosmetic()

        # 2. Click on first product of the list
        cosmetic_page_object.click_first_product()

        # 3. Add product to favourites
        product_page_object.add_to_favourites()
        wait.until(EC.text_to_be_present_in_element(Locators.FAVOURITES_MESSAGE, "Masz w ulubionych"))

        # 4. Verify if product was added to favourites
        favourite_message = product_page_object.verify_favourites_message()
        print(f"Favourite message: {favourite_message}.")
        assert "Masz w ulubionych" in favourite_message

        # 5. Verify if product appears in favourites on the top of the page in mini icon
        count = product_page_object.verify_favourites_message_mini()
        print(f"Number of products added to favourites: {count}.")
        assert count > 0, "Product was not added to favourites"

        # 6. Go to page with all favourites products
        product_page_object.click_all_favourites()

        # 7. Verify if correct product was added to favourites
        favourites_page_description = favourites_all_page_object.get_favourites_page_description()
        print(f"Product type added to favourites: {favourites_page_description}.")
        assert "krem" in favourites_page_description, "Face cream was not added to favourites"





