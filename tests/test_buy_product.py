import pytest
from pages.market_main_page import MarketPage


@pytest.mark.smoke
@pytest.mark.usefixtures('user_login')
class TestBuyProduct:
    def test_buy_product(self, browser):
        p = MarketPage(browser)
        p.add_to_cart(0)
        p.follow_to_basket()
        p.checkout()