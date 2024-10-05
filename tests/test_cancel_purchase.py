import pytest
from pages.market_main_page import MarketPage
from Locators.basket_page import Basket


@pytest.mark.regression
@pytest.mark.usefixtures('user_login')
class TestRemoveProduct:
    def test_remove_product(self, browser):
        p = MarketPage(browser)
        p.add_to_cart(0)
        p.add_to_cart(1)
        p.follow_to_basket()
        p.assertions.elements_count(Basket.CART_ITEM, 2, '')
        p.remove_from_cart(0)
        p.assertions.elements_count(Basket.CART_ITEM, 1, '')