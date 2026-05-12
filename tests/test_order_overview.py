import allure

from pytest import mark
from pages.complete_page import CompletePage
from pages.cart_page import CartPage
from pages.catalog_page import CatalogPage
from pages.order_overview_page import OrderOverviewPage
from pages.checkout_page import CheckoutPage
from tests.test_data.datasets import Datasets
from tests.test_data.pages_data import CatalogData
from tests.test_data.user_data import UserData
from tests.test_data.expected_values import ExpectedValues as EV
from utils.assertion import Assert


class TestOverViewPage:
    @classmethod
    def setup_class(cls):
        cls.catalog = CatalogPage(cls.driver)
        cls.cart = CartPage(cls.driver)
        cls.checkout_page = CheckoutPage(cls.driver)
        cls.overview = OrderOverviewPage(cls.driver)
        cls.complete = CompletePage(cls.driver)

    def _filling_user_data(self):
        self.checkout_page.filling_fields(
            UserData.FIRST_NAME,
            UserData.SECOND_NAME,
            UserData.MIDDLE_NAME,
            UserData.ADDRESS,
            UserData.CART_NUMBER
        )

    @allure.feature('DATA MATCH')
    @allure.story('Проверка соответствия поля "Имя"')
    @mark.smoke
    @mark.parametrize('test_product', ['sandwich'], indirect=True)
    def test_first_name_matching(self, test_product, auth_by_user1):
        self.catalog.open()
        self.catalog.add_product(test_product.name)
        self.cart.open()
        self.cart.click_place_an_order_button()
        self._filling_user_data()
        self.checkout_page.click_place_an_order_button()

        Assert.compare_values(
            value_name='First name (match)',
            current_value=self.overview.get_first_name(),
            expected_value=UserData.FIRST_NAME
        )

    @allure.feature('DATA MATCH')
    @allure.story('Проверка соответствия поля "Фамилия"')
    @mark.smoke
    @mark.parametrize('test_product', ['sandwich'], indirect=True)
    def test_second_name_matching(self, test_product, auth_by_user1):
        self.catalog.open()
        self.catalog.add_product(test_product.name)
        self.cart.open()
        self.cart.click_place_an_order_button()
        self._filling_user_data()
        self.checkout_page.click_place_an_order_button()

        Assert.compare_values(
            value_name='Second name (match)',
            current_value=self.overview.get_second_name(),
            expected_value=UserData.SECOND_NAME
        )

    @allure.feature('DATA MATCH')
    @allure.story('Проверка соответствия поля "Отчество"')
    @mark.smoke
    @mark.parametrize('test_product', ['sandwich'], indirect=True)
    def test_middle_name_matching(self, test_product, auth_by_user1):
        self.catalog.open()
        self.catalog.add_product(test_product.name)
        self.cart.open()
        self.cart.click_place_an_order_button()
        self._filling_user_data()
        self.checkout_page.click_place_an_order_button()

        Assert.compare_values(
            value_name='Middle name (match)',
            current_value=self.overview.get_middle_name(),
            expected_value=UserData.MIDDLE_NAME
        )

    @allure.feature('DATA MATCH')
    @allure.story('Проверка соответствия списка продуктов')
    @mark.smoke
    @mark.parametrize(
        'test_products',
        [['sandwich', 'nuggets']],
        indirect=True
    )
    def test_products_list_matching(self, test_products, auth_by_user1):
        self.catalog.open()
        for product in test_products:
            self.catalog.add_product(product.name)

        self.cart.open()
        self.cart.click_place_an_order_button()
        self._filling_user_data()
        self.checkout_page.click_place_an_order_button()

        Assert.compare_values(
            value_name='Product list (match)',
            current_value=set(self.overview.get_products_title()),
            expected_value=set(product.name for product in test_products)
        )

    @allure.feature('DATA MATCH')
    @allure.story('Проверка соответствия количества товаров')
    @mark.smoke
    @mark.parametrize(
        'test_products',
        [['sandwich', 'nuggets']],
        indirect=True
    )
    @mark.parametrize(
        'quantities',
        Datasets.ORDER_OVERVIEW_QUANTITIES_OF_PRODUCTS
    )
    def test_count_of_product_matching(
            self,
            test_products,
            quantities,
            auth_by_user1,
            product_count_to_cart
    ):
        for i in range(len(test_products)):
            product_count_to_cart(test_products[i], quantities[i])

        self.cart.open()
        self.cart.click_place_an_order_button()
        self._filling_user_data()
        self.checkout_page.click_place_an_order_button()

        for i in range(len(test_products)):
            product_name = test_products[i].name
            Assert.compare_values(
                value_name=f'Count of product: {product_name} (match)',
                current_value=self.overview.get_product_count(product_name),
                expected_value=quantities[i]
            )

    @allure.feature('DATA MATCH')
    @allure.story('Проверка соответствия цены товаров')
    @mark.smoke
    @mark.parametrize('test_product', ['sandwich'], indirect=True)
    def test_price_of_product_matching(self, test_product, auth_by_user1):
        self.catalog.open()
        self.catalog.add_product(test_product.name)
        self.cart.open()
        self.cart.click_place_an_order_button()
        self._filling_user_data()
        self.checkout_page.click_place_an_order_button()

        Assert.compare_values(
            value_name='Product price (match)',
            current_value=self.overview.get_product_price(test_product.name),
            expected_value=test_product.get_price_str()
        )

    @allure.feature('DATA MATCH')
    @allure.story('Проверка соответствия адреса доставки')
    @mark.smoke
    @mark.parametrize('test_product', ['sandwich'], indirect=True)
    def test_delivery_address_matching(self, test_product, auth_by_user1):
        self.catalog.open()
        self.catalog.add_product(test_product.name)
        self.cart.open()
        self.cart.click_place_an_order_button()
        self._filling_user_data()
        self.checkout_page.click_place_an_order_button()

        Assert.compare_values(
            value_name='Delivery address (match)',
            current_value=self.overview.get_delivery_address(),
            expected_value=UserData.ADDRESS
        )

    @allure.feature('DATA MATCH')
    @allure.story('Проверка соответствия номера карты')
    @mark.smoke
    @mark.parametrize('test_product', ['sandwich'], indirect=True)
    def test_cart_number_matching(self, test_product, auth_by_user1):
        self.catalog.open()
        self.catalog.add_product(test_product.name)
        self.cart.open()
        self.cart.click_place_an_order_button()
        self._filling_user_data()
        self.checkout_page.click_place_an_order_button()

        Assert.compare_values(
            value_name='Cart number (match)',
            current_value=self.overview.get_cart_number(),
            expected_value=UserData.CART_NUMBER
        )

    @allure.feature('OPERATIONS')
    @allure.story('Проверка итогового количества товаров')
    @mark.smoke
    @mark.parametrize(
        'test_products',
        [['sandwich', 'nuggets']],
        indirect=True
    )
    @mark.parametrize(
        'quantities',
        Datasets.ORDER_OVERVIEW_QUANTITIES_OF_PRODUCTS
    )
    def test_total_count(
            self,
            test_products,
            quantities,
            auth_by_user1,
            product_count_to_cart
    ):
        for i in range(len(test_products)):
            product_count_to_cart(test_products[i], quantities[i])

        self.cart.open()
        self.cart.click_place_an_order_button()
        self._filling_user_data()
        self.checkout_page.click_place_an_order_button()

        Assert.compare_values(
            value_name='Total count of products',
            current_value=self.overview.get_total_count(),
            expected_value=sum(quantities)
        )

    @allure.feature('OPERATIONS')
    @allure.story('Проверка итоговой стоимости заказа')
    @mark.smoke
    @mark.parametrize(
        'test_products',
        [['sandwich', 'nuggets']],
        indirect=True
    )
    @mark.parametrize(
        'quantities',
        Datasets.ORDER_OVERVIEW_QUANTITIES_OF_PRODUCTS
    )
    def test_total_cost(
            self,
            test_products,
            quantities,
            auth_by_user1,
            product_count_to_cart
    ):
        expected_total_cost = 0
        for i in range(len(test_products)):
            product_count_to_cart(test_products[i], quantities[i])
            expected_total_cost += test_products[i].price * quantities[i]

        self.cart.open()
        self.cart.click_place_an_order_button()
        self._filling_user_data()
        self.checkout_page.click_place_an_order_button()

        Assert.compare_values(
            value_name='Total cost of products',
            current_value=self.overview.get_total_cost(),
            expected_value=EV.OVERVIEW_TOTAL_COST_TO_STRING(
                expected_total_cost
            )
        )

    @allure.feature('NAVIGATION')
    @allure.story('Проверка перехода обратно в каталог')
    @mark.parametrize('test_product', ['sandwich'], indirect=True)
    def test_navigate_back_to_catalog(self, test_product, auth_by_user1):
        self.catalog.open()
        self.catalog.add_product(test_product.name)
        self.cart.open()
        self.cart.click_place_an_order_button()
        self._filling_user_data()
        self.checkout_page.click_place_an_order_button()
        self.overview.click_back_to_catalog_button()

        Assert.check_header(self.catalog, CatalogData.HEADER)
        Assert.check_url(self.catalog)
