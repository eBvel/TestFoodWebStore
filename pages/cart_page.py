import allure

from selenium.common import TimeoutException
from pages.base_page import BasePage
from utils.assertion import Assert
from webstore_config.links import Links
from webstore_config.locators import CartLocators as locators


class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = Links.CART_PAGE_URL

    @allure.step('Запрос текста "сообщения" о пустой корзине')
    def get_cart_is_empty_text(self):
        return self.find_visible_element(locators.CART_IS_EMPTY_TEXT).text

    @allure.step('Запрос, пустая корзина или нет')
    def is_empty(self):
        try:
            self.find_visible_element(locators.CART_IS_EMPTY_TEXT)
            return True
        except TimeoutException:
            return False

    @allure.step('Запрос, отображается поле "итоговая стоимость" '
                 'в корзине или нет')
    def total_cost_is_displayed(self):
        return self.find_visible_element(locators.TOTAL_COST).is_displayed()

    @allure.step('Запрос, отображается кнопка "Оформить заказ" или нет')
    def place_an_order_button_is_display(self):
        try:
            return (
                self
                .find_visible_element(locators.PLACE_AN_ORDER_BUTTON)
                .is_displayed()
            )
        except TimeoutException:
            return False

    def get_product_price(self, product_name):
        with allure.step(f'Запрос "цены" товара "{product_name}" в корзине'):
            return (
                self
                .find_visible_element(locators.PRODUCT_PRICE(product_name))
                .text
            )

    def multiple_button_click(self, product_name, locator, click_count=1):
        for i in range(click_count):
            self.click(locator)
            self.is_attribute_present(
                locators.COUNT_OF_PRODUCT(product_name),
                'value',
                str(i+1)
            )

    def add_product(self, product_name, count=1):
        with allure.step(f'Добавление товара "{product_name}" '
                         f'в количестве "{count}" в корзинку'):
            self.multiple_button_click(
                product_name,
                locators.ADD_BUTTON(product_name),
                count
            )

    def remove_product(self, product_name, count=1):
        with allure.step(f'Удаление товара "{product_name}"'
                         f'в количестве "{count}" из корзинки'):
            self.multiple_button_click(
                product_name,
                locators.REMOVE_BUTTON(product_name),
                count
            )

    def get_product_count(self, product_name):
        with allure.step(f'Запрос кол-ва товара "{product_name}" в корзинке'):
            return int(
                self
               .find_visible_element(locators.COUNT_OF_PRODUCT(product_name))
               .get_attribute('value')
            )

    @allure.step('Запрос "итоговой стоимости" товаров в корзине')
    def get_total_cost(self):
        return self.find_visible_element(locators.TOTAL_COST).text

    @allure.step('Нажатие кнопки "Оформить заказ"')
    def click_place_an_order_button(self):
        self.click(locators.PLACE_AN_ORDER_BUTTON)

    def check_product_price(self, product_name, expected_value):
        with allure.step(f'Проверка "цены" товара "{product_name}" '
                         f'в корзине'):
            cart_product_price = self.get_product_price(product_name)
            Assert.compare_values(
                f"CART: Product price ({product_name})",
                cart_product_price,
                expected_value
            )

    def check_total_cost_display(self, expected_value):
        with allure.step('Проверка отображения кнопки "Оформить заказ".'
                         f'Ожидаемый результат: {expected_value}'):
            Assert.compare_values(
                "CART: Total cost is display",
                self.total_cost_is_displayed(),
                expected_value
            )

    def check_cart_is_empty_text(self, expected_value):
        with allure.step('Проверка текста "сообщения" о пустой корзине. '
                         f'Ожидаемый результат: {expected_value}'):
            Assert.compare_values(
                "CART: Empty text",
                self.get_cart_is_empty_text(),
                expected_value
            )

    def check_total_cost(self, expected_value):
        with allure.step('Проверка поля "итоговая стоимость" в корзине. '
                         f'Ожидаемое значение: {expected_value}'):
            Assert.compare_values(
                "CART: Total cost",
                self.get_total_cost(),
                expected_value
            )

    def check_cart_is_empty(self, expected_value):
        with allure.step('Проверка корзины на пустоту. '
                         f'Ожидаемое значение: {expected_value}'):
            Assert.compare_values(
                "CART: Cart is empty",
                self.is_empty(),
                expected_value
            )

    def check_product_count(self, product_name, expected_value):
        with allure.step(f'Проверка "количества" товара "{product_name}" '
                         f'в корзине. Ожидаемое значение: {expected_value}'):
            self.is_attribute_present(
                locators.COUNT_OF_PRODUCT(product_name),
                'value',
                str(expected_value)
            )
            Assert.compare_values(
                f"CART: Product count ({product_name})",
                self.get_product_count(product_name),
                expected_value
            )

    def check_place_an_order_button_display(self, expected_value):
        with allure.step('Проверка отображения кнопки "Оформить заказ". '
                         f'Ожидаемое значение: {expected_value}'):
            Assert.compare_values(
                "CART: Place an order button is display",
                self.place_an_order_button_is_display(),
                expected_value
            )