import allure

from pytest import mark
from pages.complete_page import CompletePage
from tests.test_data import headers, checkout_data
from pages.cart_page import CartPage
from pages.catalog_page import CatalogPage
from pages.order_overview_page import OrderOverviewPage
from pages.checkout_page import CheckoutPage


class TestCompletePage:
    @classmethod
    def setup_class(cls):
        cls.catalog = CatalogPage(cls.driver)
        cls.cart = CartPage(cls.driver)
        cls.checkout_page = CheckoutPage(cls.driver)
        cls.overview = OrderOverviewPage(cls.driver)
        cls.complete = CompletePage(cls.driver)

    def _filling_user_data(self):
        self.checkout_page.filling_fields(
            checkout_data.FIRST_NAME,
            checkout_data.SECOND_NAME,
            checkout_data.MIDDLE_NAME,
            checkout_data.ADDRESS,
            checkout_data.CART_NUMBER
        )

    @allure.feature('COMPLETE ORDER')
    @allure.story('Проверка оформления заказа с корректными данными')
    @mark.parametrize('test_product', ['sandwich'], indirect=True)
    def test_complete_order(self, test_product, auth_by_user1):
        self.catalog.open()
        self.catalog.add_product(test_product.name)

        self.cart.open()
        self.cart.click_place_an_order_button()

        self._filling_user_data()
        self.checkout_page.click_place_an_order_button()

        self.overview.click_complete_order_button()

        self.complete.check_url()
        self.complete.check_header(headers.COMPLETE_PAGE)

        #EXPECTED_VALUE
        self.complete.check_complete_message("Ваш заказ успешно создан")

    @allure.feature('NAVIGATION')
    @allure.story('Проверка перехода обратно в каталог товаров')
    @mark.parametrize('test_product', ['sandwich'], indirect=True)
    def test_navigate_back_to_catalog(self, test_product, auth_by_user1):
        self.catalog.open()
        self.catalog.add_product(test_product.name)

        self.cart.open()
        self.cart.click_place_an_order_button()

        self._filling_user_data()
        self.checkout_page.click_place_an_order_button()

        self.overview.click_complete_order_button()
        self.complete.click_back_to_catalog_button()

        self.catalog.check_url()
        self.catalog.check_header(headers.CATALOG_PAGE)