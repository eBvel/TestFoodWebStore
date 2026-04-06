import allure
import pytest

from pages.cart_page import CartPage
from pages.catalog_page import CatalogPage
from pages.checkout_page import CheckoutPage
from tests.conftest import auth_by_user
from tests.test_data import headers, product_data, cart_data


@pytest.mark.parametrize('driver', ['CHROME', 'FIREFOX'], indirect=True)
class TestCartPage:
    def setup_method(self):
        self.catalog = CatalogPage(self.driver)
        self.cart = CartPage(self.driver)
        self.user_data = CheckoutPage(self.driver)

    @allure.feature('EMPTY TEXT')
    @allure.story('Проверка содержания сообщения, когда в корзине нет товаров')
    def test_cart_is_empty_text(self, auth_by_user):
        self.cart.open()

        if not self.cart.is_empty():
            self.cart.clear_all_products()
        self.cart.check_cart_is_empty_text(cart_data.EMPTY_TEXT)

    @allure.feature('PRODUCT DATA MATCHING')
    @allure.story('Сравнение "цены" товара в каталоге и корзине')
    def test_price_matching(self, auth_by_user):
        self.catalog.open()
        self.catalog.add_product(product_data.NAME)
        self.cart.open()
        self.cart.check_product_price(
            product_data.NAME,
            self.catalog.get_product_price(product_data.NAME)
        )

    @allure.feature('TOTAL COST')
    @allure.story('Проверка наличия поля "итоговая стоимость" в корзине')
    def test_total_cost_display(self, auth_by_user):
        self.catalog.open()
        self.catalog.add_product(product_data.NAME)
        self.cart.open()
        self.cart.check_total_cost_display(expected_value=True)

    @allure.feature('TOTAL COST')
    @allure.story('Проверка расчета "итоговой стоимости" товаров')
    def test_calculation_total_cost(self, auth_by_user):
        self.catalog.open()
        self.catalog.clear_all_products_counter()
        self.catalog.add_product(product_data.NAME, 10)
        self.cart.open()
        self.cart.check_total_cost(cart_data.EXPECTED_TOTAL_COST)

    @allure.feature('TOTAL COST')
    @allure.story('Проверка верхнего граничного значения для поля "итоговая стоимость"')
    def test_total_cost_limit(self, auth_by_user):
        self.catalog.open()
        self.catalog.clear_all_products_counter()
        self.catalog.add_product(product_data.CAVIAR_NAME)

        self.cart.open()
        self.cart.check_total_cost(cart_data.MAX_TOTAL_COST)

        self.cart.add_product(product_data.CAVIAR_NAME)
        self.cart.check_total_cost(cart_data.MAX_TOTAL_COST)

    @allure.feature('ADD/REMOVE PRODUCT')
    @allure.story('Проверка удаления всех товаров через "Корзинку"')
    def test_clear_cart(self, auth_by_user):
        self.catalog.open()
        self.catalog.add_product(product_data.NAME)

        self.cart.open()
        self.cart.clear_all_products()
        self.cart.check_cart_is_empty(expected_value=True)

    @allure.feature('ADD/REMOVE PRODUCT')
    @allure.story('Проверка добавления товара через "Корзинку"')
    def test_add_product_from_cart(self, auth_by_user):
        self.catalog.open()
        self.catalog.add_product(product_data.NAME)

        self.cart.open()
        current_count = self.cart.get_product_count(product_data.NAME)

        if current_count >= product_data.MAX_LIMIT:
            remove_count = current_count - product_data.MAX_LIMIT + 1
            self.cart.remove_product(product_data.NAME, remove_count)
            current_count -= remove_count

        self.cart.add_product(product_data.NAME)
        self.cart.check_product_count(product_data.NAME, current_count+1)

    @allure.feature('PLACE AN ORDER BUTTON')
    @allure.story('Проверка отображения кнопки "Оформить заказ" в пустой корзине')
    def test_place_an_order_button_display_in_empty_cart(self, auth_by_user):
        self.cart.open()
        self.cart.clear_all_products()
        self.cart.check_place_an_order_button_display(expected_value=False)

    @allure.feature('PLACE AN ORDER BUTTON')
    @allure.story('Проверка наличия кнопки "Оформить заказ" в корзине с товарами')
    def test_place_an_order_button_display(self, auth_by_user):
        self.catalog.open()
        self.catalog.add_product(product_data.NAME)
        self.cart.open()
        self.cart.check_place_an_order_button_display(expected_value=True)

    @allure.feature('PLACE AN ORDER BUTTON')
    @allure.story('Проверка перехода на страницу оформления заказа по кнопке "Оформить заказ"')
    def test_navigate_to_place_an_order_page(self, auth_by_user):
        self.catalog.open()
        self.catalog.add_product(product_data.NAME)
        self.cart.open()
        self.cart.click_place_an_order_button()
        self.user_data.check_header(headers.USER_DATA_PAGE)
