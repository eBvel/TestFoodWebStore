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
from utils.assertion import Assert


class TestCheckoutPage:
    @classmethod
    def setup_class(cls):
        cls.catalog = CatalogPage(cls.driver)
        cls.cart = CartPage(cls.driver)
        cls.checkout = CheckoutPage(cls.driver)
        cls.overview = OrderOverviewPage(cls.driver)

    @allure.feature('VALID DATA')
    @allure.story('Проверка оформления заказа с корректными данными')
    @mark.smoke
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

        Assert.check_header(self.overview, OrderOverviewData.HEADER)
        Assert.check_url(self.overview)

    @allure.feature('EMPTY FIELDS')
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

        Assert.check_header(self.checkout, CheckoutData.HEADER)
        Assert.compare_values(
            value_name='Text of empty fields message',
            current_value=self.checkout.try_get_empty_fields_alert(),
            expected_value=CheckoutData.ALL_EMPTY_FIELDS_MESSAGE
        )

    @allure.feature('INVALID DATA')
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

        Assert.compare_values(
            value_name='Second name',
            current_value=self.checkout.get_second_name(),
            expected_value=EV.CHECKOUT_EMPTY_FIELD
        )

    @allure.feature('INVALID DATA')
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

        Assert.compare_values(
            value_name='First name',
            current_value=self.checkout.get_first_name(),
            expected_value=EV.CHECKOUT_EMPTY_FIELD
        )

    @allure.feature('INVALID DATA')
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

        Assert.compare_values(
            value_name='Cart number',
            current_value=self.checkout.get_cart_number(),
            expected_value=EV.CHECKOUT_EMPTY_FIELD
        )

    @allure.feature('NAVIGATION')
    @allure.story('Проверка перехода в каталог по кнопке "Обратно в магазин"')
    @mark.parametrize('test_product', ['sandwich'], indirect=True)
    def test_navigate_back_to_catalog(self, test_product, auth_by_user1):
        self.catalog.open()
        self.catalog.add_product(test_product.name)
        self.cart.open()
        self.cart.click_place_an_order_button()
        self.checkout.click_back_to_catalog()

        Assert.check_header(self.catalog, CatalogData.HEADER)