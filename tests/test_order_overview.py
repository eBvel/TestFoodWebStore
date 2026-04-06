import allure
import pytest

from pages.complete_page import CompletePage
from tests.test_data import headers, product_data, checkout_data
from pages.cart_page import CartPage
from pages.catalog_page import CatalogPage
from pages.order_overview_page import OrderOverviewPage
from pages.checkout_page import CheckoutPage


@pytest.mark.parametrize('driver', ['CHROME', 'FIREFOX'], indirect=True)
class TestOverViewPage:
    def setup_method(self):
        self.catalog = CatalogPage(self.driver)
        self.cart = CartPage(self.driver)
        self.user_data = CheckoutPage(self.driver)
        self.overview = OrderOverviewPage(self.driver)
        self.complete = CompletePage(self.driver)

    def _filling_user_data(self):
        self.user_data.enter_first_name(checkout_data.FIRST_NAME)
        self.user_data.enter_second_name(checkout_data.SECOND_NAME)
        self.user_data.enter_middle_name(checkout_data.MIDDLE_NAME)
        self.user_data.enter_delivery_address(checkout_data.ADDRESS)
        self.user_data.enter_cart_number(checkout_data.CART_NUMBER)

    @allure.feature('USER DATA MATCHING')
    @allure.story('Проверка соответствия поля "Имя"')
    def test_first_name_matching(self, auth_by_user):
        self.catalog.open()
        self.catalog.add_product(product_data.NAME)

        self.cart.open()
        self.cart.click_place_an_order_button()

        self._filling_user_data()
        self.user_data.click_place_an_order_button()

        self.overview.check_first_name(checkout_data.FIRST_NAME)

    @allure.feature('USER DATA MATCHING')
    @allure.story('Проверка соответствия поля "Фамилия"')
    def test_second_name_matching(self, auth_by_user):
        self.catalog.open()
        self.catalog.add_product(product_data.NAME)

        self.cart.open()
        self.cart.click_place_an_order_button()

        self._filling_user_data()
        self.user_data.click_place_an_order_button()

        self.overview.check_second_name(checkout_data.SECOND_NAME)

    @allure.feature('USER DATA MATCHING')
    @allure.story('Проверка соответствия поля "Отчество"')
    def test_middle_name_matching(self, auth_by_user):
        self.catalog.open()
        self.catalog.add_product(product_data.NAME)

        self.cart.open()
        self.cart.click_place_an_order_button()

        self._filling_user_data()
        self.user_data.click_place_an_order_button()

        self.overview.check_middle_name(checkout_data.MIDDLE_NAME)

    @allure.feature('PRODUCTS DATA MATCHING')
    @allure.story('Проверка соответствия списка продуктов')
    def test_products_list_matching(self, auth_by_user):
        self.catalog.open()
        self.catalog.clear_all_products_counter()
        self.catalog.add_product(product_data.NAME)
        self.catalog.add_product(product_data.s_NAME)

        self.cart.open()
        self.cart.click_place_an_order_button()

        self._filling_user_data()
        self.user_data.click_place_an_order_button()

        self.overview.check_products_list(
            [product_data.NAME, product_data.s_NAME]
        )

    @allure.feature('PRODUCTS DATA MATCHING')
    @allure.story('Проверка соответствия количества товаров')
    def test_count_of_product_matching(self, auth_by_user):
        self.catalog.open()
        self.catalog.clear_all_products_counter()
        self.catalog.add_product(product_data.NAME, 5)
        # self.catalog.add_product(product_data.s_NAME, 3)

        self.cart.open()
        self.cart.click_place_an_order_button()

        self._filling_user_data()
        self.user_data.click_place_an_order_button()

        self.overview.check_products_count(product_data.NAME, 5)

    @allure.feature('PRODUCTS DATA MATCHING')
    @allure.story('Проверка соответствия цены товаров')
    def test_price_of_product_matching(self, auth_by_user):
        self.catalog.open()
        self.catalog.clear_all_products_counter()
        self.catalog.add_product(product_data.NAME)

        self.cart.open()
        self.cart.click_place_an_order_button()

        self._filling_user_data()
        self.user_data.click_place_an_order_button()

        self.overview.check_products_price(product_data.NAME, product_data.PRICE)

    @allure.feature('USER DATA MATCHING')
    @allure.story('Проверка соответствия адреса доставки')
    def test_delivery_address_matching(self, auth_by_user):
        self.catalog.open()
        self.catalog.add_product(product_data.NAME)

        self.cart.open()
        self.cart.click_place_an_order_button()

        self._filling_user_data()
        self.user_data.click_place_an_order_button()

        self.overview.check_delivery_address(checkout_data.ADDRESS)

    @allure.feature('USER DATA MATCHING')
    @allure.story('Проверка соответствия номера карты')
    def test_cart_number_matching(self, auth_by_user):
        self.catalog.open()
        self.catalog.add_product(product_data.NAME)

        self.cart.open()
        self.cart.click_place_an_order_button()

        self._filling_user_data()
        self.user_data.click_place_an_order_button()

        self.overview.check_cart_number(checkout_data.CART_NUMBER)

    @allure.feature('TOTAL DATA OF ORDER')
    @allure.story('Проверка итогового количества товаров')
    def test_total_count(self, auth_by_user):
        self.catalog.open()
        self.catalog.clear_all_products_counter()
        self.catalog.add_product(product_data.NAME)

        self.cart.open()
        self.cart.click_place_an_order_button()

        self._filling_user_data()
        self.user_data.click_place_an_order_button()

        self.overview.check_total_count(1)

    @allure.feature('TOTAL DATA OF ORDER')
    @allure.story('Проверка итоговой стоимости заказа')
    def test_total_cost(self, auth_by_user):
        self.catalog.open()
        self.catalog.clear_all_products_counter()
        self.catalog.add_product(product_data.NAME)

        self.cart.open()
        self.cart.click_place_an_order_button()

        self._filling_user_data()
        self.user_data.click_place_an_order_button()

        #EXPECTED_VALUE
        self.overview.check_total_cost(product_data.PRICE)

    @allure.feature('NAVIGATION')
    @allure.story('Проверка перехода обратно в каталог')
    def test_navigate_back_to_catalog(self):
        self.catalog.open()
        self.catalog.add_product(product_data.NAME)

        self.cart.open()
        self.cart.click_place_an_order_button()

        self._filling_user_data()
        self.user_data.click_place_an_order_button()

        self.overview.click_back_to_catalog_button()
        self.catalog.check_header(headers.CATALOG_PAGE)
