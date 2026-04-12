import allure

from pages.complete_page import CompletePage
from tests.test_data import headers, product_data, checkout_data
from pages.cart_page import CartPage
from pages.catalog_page import CatalogPage
from pages.order_overview_page import OrderOverviewPage
from pages.checkout_page import CheckoutPage


class TestCompletePage:

    @classmethod
    def setup_class(cls):
        cls.catalog = CatalogPage(cls.driver)
        cls.cart = CartPage(cls.driver)
        cls.user_data = CheckoutPage(cls.driver)
        cls.overview = OrderOverviewPage(cls.driver)
        cls.complete = CompletePage(cls.driver)

    def _filling_user_data(self):
        self.user_data.enter_first_name(checkout_data.FIRST_NAME)
        self.user_data.enter_second_name(checkout_data.SECOND_NAME)
        self.user_data.enter_middle_name(checkout_data.MIDDLE_NAME)
        self.user_data.enter_delivery_address(checkout_data.ADDRESS)
        self.user_data.enter_cart_number(checkout_data.CART_NUMBER)

    @allure.feature('COMPLETE ORDER')
    @allure.story('Проверка оформления заказа с корректными данными')
    def test_complete_order(self, auth_by_user1):
        self.catalog.open()
        self.catalog.add_product(product_data.NAME)

        self.cart.open()
        self.cart.click_place_an_order_button()

        self._filling_user_data()
        self.user_data.click_place_an_order_button()

        self.overview.click_complete_order_button()
        # страница не пролистывается (вниз) до кнопки в браузере Mozilla

        self.complete.check_url()
        self.complete.check_header(headers.COMPLETE_PAGE)

        # EXPECTED_VALUE
        self.complete.check_complete_message("Ваш заказ успешно создан")

    @allure.feature('NAVIGATION')
    @allure.story('Проверка перехода обратно в каталог товаров')
    def test_navigate_back_to_catalog(self):
        self.catalog.open()
        self.catalog.add_product(product_data.NAME)

        self.cart.open()
        self.cart.click_place_an_order_button()

        self._filling_user_data()
        self.user_data.click_place_an_order_button()

        self.overview.click_complete_order_button()
        self.complete.click_back_to_catalog_button()

        self.catalog.check_url()
        self.catalog.check_header(headers.CATALOG_PAGE)