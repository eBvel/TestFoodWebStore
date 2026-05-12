import allure

from selenium.common import TimeoutException
from pages.base_page import BasePage
from utils.assertion import Assert
from webstore_config.links import Links
from webstore_config.locators import UserDataLocators as locators


class CheckoutPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = Links.PLACE_AN_ORDER_PAGE_URL

    def __fill_in_field(self, field_name, value, locator):
        with allure.step(f'Ввод значения "{value}" в поле "{field_name}"'):
            (
                self
                .find_visible_element(locator)
                .send_keys(value if value is not None else '')
            )

    def enter_first_name(self, first_name):
        self.__fill_in_field('Имя', first_name, locators.FIRST_NAME_FIELD)

    def enter_second_name(self, second_name):
        self.__fill_in_field(
            'Фамилия',
            second_name,
            locators.SECOND_NAME_FIELD
        )

    def enter_middle_name(self, middle_name):
        self.__fill_in_field(
            'Отчество',
            middle_name,
            locators.MIDDLE_NAME_FIELD
        )

    def enter_delivery_address(self, address):
        self.__fill_in_field(
            'Адрес доставки',
            address,
            locators.DELIVERY_ADDRESS_FIELD
        )

    def enter_cart_number(self, cart_number):
        self.__fill_in_field(
            'Номер карты',
            cart_number,
            locators.CART_NUMBER_FIELD
        )

    def filling_fields(
            self,
            first_name,
            second_name,
            middle_name,
            delivery_address,
            cart_number
    ):
        self.enter_first_name(first_name)
        self.enter_second_name(second_name)
        self.enter_middle_name(middle_name)
        self.enter_delivery_address(delivery_address)
        self.enter_cart_number(cart_number)

    @allure.step('Нажатие кнопки "Оформить заказ"')
    def click_place_an_order_button(self):
        self.click(locators.PLACE_AN_ORDER_BUTTON)

    @allure.step('Нажатие кнопки "Обратно в магазин"')
    def click_back_to_catalog(self):
        self.click(locators.BACK_TO_CATALOG_BUTTON)

    @allure.step('Запрос значения из поля "Имя"')
    def get_first_name(self):
        return (
            self
            .find_visible_element(locators.FIRST_NAME_FIELD)
            .get_attribute('value')
        )

    @allure.step('Запрос значения из поля "Фамилия"')
    def get_second_name(self):
        return (
            self
            .find_visible_element(locators.SECOND_NAME_FIELD)
            .get_attribute('value')
        )

    @allure.step('Запрос значения из поля "Номер карты"')
    def get_cart_number(self):
        return (
            self
            .find_visible_element(locators.CART_NUMBER_FIELD)
            .get_attribute('value')
        )

    @allure.step('Попытка получить текст уведомления о пустых полях')
    def try_get_empty_fields_alert(self):
        try:
            return self.find_visible_element(locators.EMPTY_FIELDS_ALERT).text
        except TimeoutException:
            return None

    def check_empty_fields_alert(self, expected_value):
        with allure.step(f'Проверка текста уведомления о пустых полях. '
                         f'Ожидаемое значение: f"{expected_value}"'):
            Assert.compare_values(
                "CHECKOUT: Empty field alert",
                self.try_get_empty_fields_alert(),
                expected_value
            )

    def check_first_name(self, expected_value):
        with allure.step(f'Проверка поля "Имя". Ожидаемое значение: '
                         f'f"{expected_value}"'):
            Assert.compare_values(
                "CHECKOUT: First name",
                self.get_first_name(),
                expected_value
            )

    def check_second_name(self, expected_value):
        with allure.step(f'Проверка поля "Фамилия". Ожидаемое значение: '
                         f'f"{expected_value}"'):
            Assert.compare_values(
                "CHECKOUT: Second name",
                self.get_second_name(),
                expected_value
            )

    def check_cart_number(self, expected_value):
        with allure.step(f'Проверка поля "Номер карты". Ожидаемое значение: '
                         f'f"{expected_value}"'):
            Assert.compare_values(
                "CHECKOUT: Cart number",
                self.get_cart_number(),
                expected_value
            )