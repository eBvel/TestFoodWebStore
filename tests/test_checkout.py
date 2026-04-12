import allure
import pytest

from pages.cart_page import CartPage
from pages.catalog_page import CatalogPage
from pages.order_overview_page import OrderOverviewPage
from pages.checkout_page import CheckoutPage
from tests.test_data import headers, product_data, checkout_data


class TestUserDataPage:

    @classmethod
    def setup_class(cls):
        cls.catalog = CatalogPage(cls.driver)
        cls.cart = CartPage(cls.driver)
        cls.checkout = CheckoutPage(cls.driver)
        cls.overview = OrderOverviewPage(cls.driver)

    @allure.feature('PLACE AN ORDER')
    @allure.story('Проверка оформления заказа с корректными данными')
    def test_filling_fields_with_valid_data(self, auth_by_user1):
        self.catalog.open()
        self.catalog.add_product(product_data.NAME)

        self.cart.open()
        self.cart.click_place_an_order_button()

        self.checkout.enter_second_name(checkout_data.SECOND_NAME)
        self.checkout.enter_first_name(checkout_data.FIRST_NAME)
        self.checkout.enter_middle_name(checkout_data.MIDDLE_NAME)
        self.checkout.enter_delivery_address(checkout_data.ADDRESS)
        self.checkout.enter_cart_number(checkout_data.CART_NUMBER)

        self.checkout.click_place_an_order_button()
        self.overview.check_header(headers.ORDER_OVERVIEW_PAGE)

    @allure.feature('PLACE AN ORDER')
    @allure.story('Проверка оформления заказа с пустыми полями')
    def test_place_an_order_with_empty_fields(self, auth_by_user1):
        self.catalog.open()
        self.catalog.add_product(product_data.NAME)

        self.cart.open()
        self.cart.click_place_an_order_button()

        self.checkout.click_place_an_order_button()
        self.checkout.check_header(headers.USER_DATA_PAGE)
        self.checkout.check_empty_fields_alert(
            checkout_data.ALL_EMPTY_FIELDS_MESSAGE
        )

    @allure.feature('FIELDS VALIDATION')
    @allure.story('Проверка валидации поля "Фамилия"')
    @pytest.mark.parametrize('value', checkout_data.NAMES_DATASET)
    def test_validation_of_second_name(self, auth_by_user1, value):
        self.catalog.open()
        self.catalog.add_product(product_data.NAME)

        self.cart.open()
        self.cart.click_place_an_order_button()

        self.checkout.enter_second_name(value)
        self.checkout.check_second_name(expected_value="")

    @allure.feature('FIELDS VALIDATION')
    @allure.story('Проверка валидации поля "Имя"')
    @pytest.mark.parametrize('value', checkout_data.NAMES_DATASET)
    def test_validation_of_first_name(self, auth_by_user1, value):
        self.catalog.open()
        self.catalog.add_product(product_data.NAME)

        self.cart.open()
        self.cart.click_place_an_order_button()

        self.checkout.enter_first_name(value)
        self.checkout.check_first_name(expected_value="")

    @allure.feature('FIELDS VALIDATION')
    @allure.story('Проверка валидации поля "Номер карты"')
    @pytest.mark.parametrize('value', checkout_data.CART_DATASET)
    def test_validation_of_cart_number(self, auth_by_user1, value):
        self.catalog.open()
        self.catalog.add_product(product_data.NAME)

        self.cart.open()
        self.cart.click_place_an_order_button()

        self.checkout.enter_cart_number(value)
        self.checkout.check_cart_number(expected_value="")

    @allure.feature('NAVIGATION')
    @allure.story('Проверка перехода в каталог по кнопке "Обратно в магазин"')
    def test_navigate_back_to_catalog(self, auth_by_user1):
        self.catalog.open()
        self.catalog.add_product(product_data.NAME)

        self.cart.open()
        self.cart.click_place_an_order_button()

        self.checkout.click_back_to_catalog()
        self.catalog.check_header(headers.CATALOG_PAGE)