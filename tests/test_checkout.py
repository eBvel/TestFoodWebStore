import allure

from pytest import mark
from pages.cart_page import CartPage
from pages.catalog_page import CatalogPage
from pages.order_overview_page import OrderOverviewPage
from pages.checkout_page import CheckoutPage
from tests.test_data.datasets import Datasets
from tests.test_data.user_data import UserData
from tests.test_data.pages_data import (CheckoutData, OrderOverviewData,
                                        CatalogData)
from tests.test_data.expected_values import ExpectedValues as EV


class TestUserDataPage:
    @classmethod
    def setup_class(cls):
        cls.catalog = CatalogPage(cls.driver)
        cls.cart = CartPage(cls.driver)
        cls.checkout = CheckoutPage(cls.driver)
        cls.overview = OrderOverviewPage(cls.driver)

    @allure.feature('PLACE AN ORDER')
    @allure.story('Проверка оформления заказа с корректными данными')
    @mark.parametrize('test_product', ['sandwich'], indirect=True)
    def test_filling_fields_with_valid_data(
            self,
            test_product,
            auth_by_user1
    ):
        self.catalog.open()
        self.catalog.add_product(test_product.name)
        self.cart.open()
        self.cart.click_place_an_order_button()
        self.checkout.filling_fields(
            UserData.SECOND_NAME,
            UserData.FIRST_NAME,
            UserData.MIDDLE_NAME,
            UserData.ADDRESS,
            UserData.CART_NUMBER
        )
        self.checkout.click_place_an_order_button()

        self.overview.check_header(OrderOverviewData.HEADER)

    @allure.feature('PLACE AN ORDER')
    @allure.story('Проверка оформления заказа с пустыми полями')
    @mark.parametrize('test_product', ['sandwich'], indirect=True)
    def test_place_an_order_with_empty_fields(
            self,
            test_product,
            auth_by_user1
    ):
        self.catalog.open()
        self.catalog.add_product(test_product.name)
        self.cart.open()
        self.cart.click_place_an_order_button()
        self.checkout.click_place_an_order_button()

        self.checkout.check_header(CheckoutData.HEADER)
        self.checkout.check_empty_fields_alert(
            CheckoutData.ALL_EMPTY_FIELDS_MESSAGE
        )

    @allure.feature('FIELDS VALIDATION')
    @allure.story('Проверка валидации поля "Фамилия"')
    @mark.parametrize('test_product', ['sandwich'], indirect=True)
    @mark.parametrize('value', Datasets.CHECKOUT_INCORRECT_NAMES)
    def test_validation_of_second_name(
            self,
            test_product,
            value,
            auth_by_user1
    ):
        self.catalog.open()
        self.catalog.add_product(test_product.name)
        self.cart.open()
        self.cart.click_place_an_order_button()
        self.checkout.enter_second_name(value)

        self.checkout.check_second_name(EV.CHECKOUT_EMPTY_FIELD)

    @allure.feature('FIELDS VALIDATION')
    @allure.story('Проверка валидации поля "Имя"')
    @mark.parametrize('test_product', ['sandwich'], indirect=True)
    @mark.parametrize('value', Datasets.CHECKOUT_INCORRECT_NAMES)
    def test_validation_of_first_name(
            self,
            test_product,
            value,
            auth_by_user1
    ):
        self.catalog.open()
        self.catalog.add_product(test_product.name)
        self.cart.open()
        self.cart.click_place_an_order_button()
        self.checkout.enter_first_name(value)

        self.checkout.check_first_name(EV.CHECKOUT_EMPTY_FIELD)

    @allure.feature('FIELDS VALIDATION')
    @allure.story('Проверка валидации поля "Номер карты"')
    @mark.parametrize('test_product', ['sandwich'], indirect=True)
    @mark.parametrize(
        'value',
        Datasets.CHECKOUT_INCORRECT_VALUES_FOR_NUMERIC_FIELD
    )
    def test_validation_of_cart_number(
            self,
            test_product,
            value,
            auth_by_user1
    ):
        self.catalog.open()
        self.catalog.add_product(test_product.name)
        self.cart.open()
        self.cart.click_place_an_order_button()
        self.checkout.enter_cart_number(value)

        self.checkout.check_cart_number(EV.CHECKOUT_EMPTY_FIELD)

    @allure.feature('NAVIGATION')
    @allure.story('Проверка перехода в каталог по кнопке "Обратно в магазин"')
    @mark.parametrize('test_product', ['sandwich'], indirect=True)
    def test_navigate_back_to_catalog(self, test_product, auth_by_user1):
        self.catalog.open()
        self.catalog.add_product(test_product.name)
        self.cart.open()
        self.cart.click_place_an_order_button()
        self.checkout.click_back_to_catalog()

        self.catalog.check_header(CatalogData.HEADER)