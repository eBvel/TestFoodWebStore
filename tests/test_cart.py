import allure

from pytest import mark
from pages.cart_page import CartPage
from pages.catalog_page import CatalogPage
from pages.checkout_page import CheckoutPage
from tests.test_data import headers, product_data, cart_data


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
        self.cart.check_cart_is_empty_text(cart_data.EMPTY_TEXT)

    @allure.feature('PRODUCT DATA MATCHING')
    @allure.story('Сравнение "цены" товара в каталоге и корзине')
    @mark.parametrize('product', ['sandwich'], indirect=True)
    def test_price_matching(self, product, auth_by_user1):
        self.catalog.open()
        self.catalog.add_product(product.name)

        self.cart.open()
        self.cart.check_product_price(
            product.name,
            product.get_price_str()
        )

    @allure.feature('TOTAL COST')
    @allure.story('Проверка наличия поля "итоговая стоимость" в корзине')
    @mark.parametrize('product', ['sandwich'], indirect=True)
    def test_total_cost_display(self, product, auth_by_user1):
        self.catalog.open()
        self.catalog.add_product(product.name)

        self.cart.open()
        self.cart.check_total_cost_display(expected_value=True)

    @allure.feature('TOTAL COST')
    @allure.story('Проверка расчета "итоговой стоимости" товаров')
    @mark.parametrize('product', ['sandwich'], indirect=True)
    def test_calculation_total_cost(self, product, auth_by_user1):
        self.catalog.open()
        self.catalog.add_product(product.name, 3)

        self.cart.open()
        self.cart.check_total_cost(f'Итого: {(product.price*3):.{0}f} ₽')

    @allure.feature('TOTAL COST')
    @allure.story('Проверка верхнего граничного значения для поля '
                  '"итоговая стоимость"')
    @mark.parametrize('product', ['caviar'], indirect=True)
    @mark.parametrize('product_count', [1, 2])
    def test_total_cost_limit(self, product_count, product, auth_by_user1):
        self.catalog.open()
        self.catalog.add_product(product.name, product_count)

        self.cart.open()
        self.cart.check_total_cost(cart_data.MAX_TOTAL_COST)

    @allure.feature('ADD/REMOVE PRODUCT')
    @allure.story('Проверка удаления всех товаров через "Корзинку"')
    @mark.parametrize('product', ['sandwich'], indirect=True)
    def test_clear_cart(self, product, auth_by_user1):
        self.catalog.open()
        self.catalog.add_product(product.name)

        self.cart.open()
        self.cart.clear_all_products()
        self.cart.check_cart_is_empty(expected_value=True)

    @allure.feature('ADD/REMOVE PRODUCT')
    @allure.story('Проверка добавления товара через "Корзинку"')
    @mark.parametrize('product', ['sandwich'], indirect=True)
    def test_add_product_from_cart(self, product, auth_by_user1):
        self.catalog.open()
        self.catalog.add_product(product.name)

        self.cart.open()
        self.cart.add_product(product.name)
        self.cart.check_product_count(product.name, 2)

    @allure.feature('PLACE AN ORDER BUTTON')
    @allure.story('Проверка отображения кнопки "Оформить заказ" '
                  'в пустой корзине')
    def test_place_an_order_button_display_in_empty_cart(self, auth_by_user1):
        self.cart.open()
        self.cart.check_place_an_order_button_display(expected_value=False)

    @allure.feature('PLACE AN ORDER BUTTON')
    @allure.story('Проверка наличия кнопки "Оформить заказ" в корзине '
                  'с товарами')
    @mark.parametrize('product', ['sandwich'], indirect=True)
    def test_place_an_order_button_display(self, product, auth_by_user1):
        self.catalog.open()
        self.catalog.add_product(product.name)

        self.cart.open()
        self.cart.check_place_an_order_button_display(expected_value=True)

    @allure.feature('PLACE AN ORDER BUTTON')
    @allure.story('Проверка перехода на страницу оформления заказа '
                  'по кнопке "Оформить заказ"')
    @mark.parametrize('product', ['sandwich'], indirect=True)
    def test_navigate_to_place_an_order_page(self, product, auth_by_user1):
        self.catalog.open()
        self.catalog.add_product(product.name)

        self.cart.open()
        self.cart.click_place_an_order_button()
        self.user_data.check_header(headers.USER_DATA_PAGE)
