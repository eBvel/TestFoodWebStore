import allure

from pytest import mark
from pages.cart_page import CartPage
from pages.catalog_page import CatalogPage
from pages.checkout_page import CheckoutPage
from tests.test_data.datasets import Datasets
from tests.test_data.pages_data import CartData, CheckoutData


class TestCartPage:
    @classmethod
    def setup_class(cls):
        cls.catalog = CatalogPage(cls.driver)
        cls.cart = CartPage(cls.driver)
        cls.user_data = CheckoutPage(cls.driver)

    @allure.feature('EMPTY TEXT')
    @allure.story('Проверка содержания сообщения, '
                  'когда в корзине нет товаров')
    def test_cart_is_empty_text(self, auth_by_user1):
        self.cart.open()
        self.cart.check_cart_is_empty_text(CartData.EMPTY_TEXT)

    @allure.feature('PRODUCT DATA MATCHING')
    @allure.story('Сравнение "цены" товара в каталоге и корзине')
    @mark.parametrize('test_product', ['sandwich'], indirect=True)
    def test_price_matching(self, test_product, auth_by_user1):
        self.catalog.open()
        self.catalog.add_product(test_product.name)

        self.cart.open()
        self.cart.check_product_price(
            test_product.name,
            test_product.get_price_str()
        )

    @allure.feature('TOTAL COST')
    @allure.story('Проверка наличия поля "итоговая стоимость" в корзине')
    @mark.parametrize('test_product', ['sandwich'], indirect=True)
    def test_total_cost_display(self, test_product, auth_by_user1):
        self.catalog.open()
        self.catalog.add_product(test_product.name)

        self.cart.open()
        #EXPECTED_VALUE
        self.cart.check_total_cost_display(expected_value=True)

    @allure.feature('TOTAL COST')
    @allure.story('Проверка расчета "итоговой стоимости" товаров')
    @mark.parametrize('test_product', ['sandwich'], indirect=True)
    @mark.parametrize('quantity', Datasets.CART_QUANTITY_OF_PRODUCT)
    def test_calculation_total_cost(self, test_product, quantity, auth_by_user1):
        self.catalog.open()
        self.catalog.add_product(test_product.name, quantity)

        self.cart.open()
        #EXPECTED_VALUE
        self.cart.check_total_cost(
            f'Итого: {(test_product.price * quantity):.{0}f} ₽'
        )

    @allure.feature('TOTAL COST')
    @allure.story('Проверка верхнего граничного значения для поля '
                  '"итоговая стоимость"')
    @mark.parametrize('test_product', ['caviar'], indirect=True)
    @mark.parametrize("count", Datasets.CART_QUANTITIES_OF_CAVIAR)
    def test_total_cost_limit(self, test_product, count, auth_by_user1):
        self.catalog.open()
        self.catalog.add_product(test_product.name, count)

        self.cart.open()
        self.cart.check_total_cost(CartData.MAX_TOTAL_COST)

    @allure.feature('ADD/REMOVE PRODUCT')
    @allure.story('Проверка удаления всех товаров через "Корзинку"')
    @mark.parametrize('test_product', ['sandwich'], indirect=True)
    def test_clear_cart(self, test_product, auth_by_user1):
        self.catalog.open()
        self.catalog.add_product(test_product.name)

        self.cart.open()
        self.cart.remove_product(test_product.name)
        #EXPECTED_VALUE
        self.cart.check_cart_is_empty(expected_value=True)

    @allure.feature('ADD/REMOVE PRODUCT')
    @allure.story('Проверка добавления товара через "Корзинку"')
    @mark.parametrize('test_product', ['sandwich'], indirect=True)
    def test_add_product_from_cart(self, test_product, auth_by_user1):
        self.catalog.open()
        self.catalog.add_product(test_product.name)

        self.cart.open()
        self.cart.add_product(test_product.name)
        #EXPECTED_VALUE
        self.cart.check_product_count(test_product.name, 2)

    @allure.feature('PLACE AN ORDER BUTTON')
    @allure.story('Проверка отображения кнопки "Оформить заказ" '
                  'в пустой корзине')
    def test_place_an_order_button_display_in_empty_cart(self, auth_by_user1):
        self.cart.open()
        #EXPECTED_VALUE
        self.cart.check_place_an_order_button_display(expected_value=False)

    @allure.feature('PLACE AN ORDER BUTTON')
    @allure.story('Проверка наличия кнопки "Оформить заказ" в корзине '
                  'с товарами')
    @mark.parametrize('test_product', ['sandwich'], indirect=True)
    def test_place_an_order_button_display(self, test_product, auth_by_user1):
        self.catalog.open()
        self.catalog.add_product(test_product.name)

        self.cart.open()
        #EXPECTED_VALUE
        self.cart.check_place_an_order_button_display(expected_value=True)

    @allure.feature('PLACE AN ORDER BUTTON')
    @allure.story('Проверка перехода на страницу оформления заказа '
                  'по кнопке "Оформить заказ"')
    @mark.parametrize('test_product', ['sandwich'], indirect=True)
    def test_navigate_to_place_an_order_page(
            self,
            test_product,
            auth_by_user1
    ):
        self.catalog.open()
        self.catalog.add_product(test_product.name)

        self.cart.open()
        self.cart.click_place_an_order_button()
        self.user_data.check_header(CheckoutData.HEADER)
