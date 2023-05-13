import unittest

from tests.cart_test import CartTest
from tests.discount_test import DiscountTest
from tests.favourites_test import FavouritesTest
from tests.refresh_test import RefreshTest
from tests.sort_test import SortTest

# Import tests which you want to run
cart_test = unittest.TestLoader().loadTestsFromTestCase(CartTest)
discount_test = unittest.TestLoader().loadTestsFromTestCase(DiscountTest)
favourites_test = unittest.TestLoader().loadTestsFromTestCase(FavouritesTest)
refresh_test = unittest.TestLoader().loadTestsFromTestCase(RefreshTest)
sort_test = unittest.TestLoader().loadTestsFromTestCase(SortTest)

# Lists of tests to be run
tests_for_run = [
    cart_test,
    discount_test,
    favourites_test,
    refresh_test,
    sort_test
]
