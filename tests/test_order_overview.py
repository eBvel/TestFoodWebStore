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

    @allure.feature('USER DATA MATCHING')
    @allure.story('Проверка соответствия поля "Имя"')
    @mark.parametrize('test_product', ['sandwich'], indirect=True)
    def test_first_name_matching(self, test_product, auth_by_user1):
        self.catalog.open()
        self.catalog.add_product(test_product.name)

        self.cart.open()
        self.cart.click_place_an_order_button()

        self._filling_user_data()
        self.checkout_page.click_place_an_order_button()

        self.overview.check_first_name(UserData.FIRST_NAME)

    @allure.feature('USER DATA MATCHING')
    @allure.story('Проверка соответствия поля "Фамилия"')
    @mark.parametrize('test_product', ['sandwich'], indirect=True)
    def test_second_name_matching(self, test_product, auth_by_user1):
        self.catalog.open()
        self.catalog.add_product(test_product.name)

        self.cart.open()
        self.cart.click_place_an_order_button()

        self._filling_user_data()
        self.checkout_page.click_place_an_order_button()

        self.overview.check_second_name(UserData.SECOND_NAME)

    @allure.feature('USER DATA MATCHING')
    @allure.story('Проверка соответствия поля "Отчество"')
    @mark.parametrize('test_product', ['sandwich'], indirect=True)
    def test_middle_name_matching(self, test_product, auth_by_user1):
        self.catalog.open()
        self.catalog.add_product(test_product.name)

        self.cart.open()
        self.cart.click_place_an_order_button()

        self._filling_user_data()
        self.checkout_page.click_place_an_order_button()

        self.overview.check_middle_name(UserData.MIDDLE_NAME)

    @allure.feature('PRODUCTS DATA MATCHING')
    @allure.story('Проверка соответствия списка продуктов')
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

        self.overview.check_products_list(
            [product.name for product in test_products]
        )

    @allure.feature('PRODUCTS DATA MATCHING')
    @allure.story('Проверка соответствия количества товаров')
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
            auth_by_user1
    ):
        self.catalog.open()

        for i in range(len(test_products)):
            self.catalog.add_product(test_products[i].name, quantities[i])

        self.cart.open()
        self.cart.click_place_an_order_button()

        self._filling_user_data()
        self.checkout_page.click_place_an_order_button()

        for i in range(len(test_products)):
            self.overview.check_products_count(
                test_products[i].name,
                quantities[i]
            )

    @allure.feature('PRODUCTS DATA MATCHING')
    @allure.story('Проверка соответствия цены товаров')
    @mark.parametrize('test_product', ['sandwich'], indirect=True)
    def test_price_of_product_matching(self, test_product, auth_by_user1):
        self.catalog.open()
        self.catalog.add_product(test_product.name)

        self.cart.open()
        self.cart.click_place_an_order_button()

        self._filling_user_data()
        self.checkout_page.click_place_an_order_button()

        self.overview.check_products_price(test_product.name, test_product.get_price_str())

    @allure.feature('USER DATA MATCHING')
    @allure.story('Проверка соответствия адреса доставки')
    @mark.parametrize('test_product', ['sandwich'], indirect=True)
    def test_delivery_address_matching(self, test_product, auth_by_user1):
        self.catalog.open()
        self.catalog.add_product(test_product.name)

        self.cart.open()
        self.cart.click_place_an_order_button()

        self._filling_user_data()
        self.checkout_page.click_place_an_order_button()

        self.overview.check_delivery_address(UserData.ADDRESS)

    @allure.feature('USER DATA MATCHING')
    @allure.story('Проверка соответствия номера карты')
    @mark.parametrize('test_product', ['sandwich'], indirect=True)
    def test_cart_number_matching(self, test_product, auth_by_user1):
        self.catalog.open()
        self.catalog.add_product(test_product.name)

        self.cart.open()
        self.cart.click_place_an_order_button()

        self._filling_user_data()
        self.checkout_page.click_place_an_order_button()

        self.overview.check_cart_number(UserData.CART_NUMBER)

    @allure.feature('TOTAL DATA OF ORDER')
    @allure.story('Проверка итогового количества товаров')
    @mark.parametrize('test_products', [['sandwich', 'nuggets']], indirect=True)
    @mark.parametrize(
        'quantities',
        Datasets.ORDER_OVERVIEW_QUANTITIES_OF_PRODUCTS
    )
    def test_total_count(self, test_products, quantities, auth_by_user1):
        self.catalog.open()

        for i in range(len(test_products)):
            self.catalog.add_product(test_products[i].name, quantities[i])

        self.cart.open()
        self.cart.click_place_an_order_button()

        self._filling_user_data()
        self.checkout_page.click_place_an_order_button()

        self.overview.check_total_count(sum(quantities))

    @allure.feature('TOTAL DATA OF ORDER')
    @allure.story('Проверка итоговой стоимости заказа')
    @mark.parametrize('test_products', [['sandwich', 'nuggets']], indirect=True)
    @mark.parametrize(
        'quantities',
        Datasets.ORDER_OVERVIEW_QUANTITIES_OF_PRODUCTS
    )
    def test_total_cost(self, test_products, quantities, auth_by_user1):
        self.catalog.open()

        expected_total_cost = 0
        for i in range(len(test_products)):
            self.catalog.add_product(test_products[i].name, quantities[i])
            expected_total_cost += test_products[i].price * quantities[i]

        self.cart.open()
        self.cart.click_place_an_order_button()

        self._filling_user_data()
        self.checkout_page.click_place_an_order_button()

        self.overview.check_total_cost(f'{expected_total_cost:.{0}f} ₽')

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
        self.catalog.check_header(CatalogData.HEADER)
