import allure

from selenium.common import TimeoutException
from pages.base_page import BasePage, WebDriver
from webstore_config.links import Links
from webstore_config.locators import UserDataLocators as locators, LocatorType


class CheckoutPage(BasePage):
    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
        self.url = Links.PLACE_AN_ORDER_PAGE_URL

    def __fill_in_field(
            self,
            field_name: str,
            value: str,
            locator: LocatorType
    ) -> None:
        with allure.step(f'Ввод значения "{value}" в поле "{field_name}"'):
            (
                self
                .find_visible_element(locator)
                .send_keys(value if value is not None else '')
            )

    def enter_first_name(self, first_name: str) -> None:
        self.__fill_in_field('Имя', first_name, locators.FIRST_NAME_FIELD)

    def enter_second_name(self, second_name: str) -> None:
        self.__fill_in_field(
            'Фамилия',
            second_name,
            locators.SECOND_NAME_FIELD
        )

    def enter_middle_name(self, middle_name: str) -> None:
        self.__fill_in_field(
            'Отчество',
            middle_name,
            locators.MIDDLE_NAME_FIELD
        )

    def enter_delivery_address(self, address: str) -> None:
        self.__fill_in_field(
            'Адрес доставки',
            address,
            locators.DELIVERY_ADDRESS_FIELD
        )

    def enter_cart_number(self, cart_number: str) -> None:
        self.__fill_in_field(
            'Номер карты',
            cart_number,
            locators.CART_NUMBER_FIELD
        )

    def filling_fields(
            self,
            first_name: str,
            second_name: str,
            middle_name: str,
            delivery_address: str,
            cart_number: str
    ) -> None:
        self.enter_first_name(first_name)
        self.enter_second_name(second_name)
        self.enter_middle_name(middle_name)
        self.enter_delivery_address(delivery_address)
        self.enter_cart_number(cart_number)

    @allure.step('Нажатие кнопки "Оформить заказ"')
    def click_place_an_order_button(self) -> None:
        self.click(locators.PLACE_AN_ORDER_BUTTON)

    @allure.step('Нажатие кнопки "Обратно в магазин"')
    def click_back_to_catalog(self) -> None:
        self.click(locators.BACK_TO_CATALOG_BUTTON)

    @allure.step('Запрос значения из поля "Имя"')
    def get_first_name(self) -> str | None:
        return (
            self
            .find_visible_element(locators.FIRST_NAME_FIELD)
            .get_attribute('value')
        )

    @allure.step('Запрос значения из поля "Фамилия"')
    def get_second_name(self) -> str | None:
        return (
            self
            .find_visible_element(locators.SECOND_NAME_FIELD)
            .get_attribute('value')
        )

    @allure.step('Запрос значения из поля "Номер карты"')
    def get_cart_number(self) -> str | None:
        return (
            self
            .find_visible_element(locators.CART_NUMBER_FIELD)
            .get_attribute('value')
        )

    @allure.step('Попытка получить текст уведомления о пустых полях')
    def try_get_empty_fields_alert(self) -> str | None:
        try:
            return self.find_visible_element(locators.EMPTY_FIELDS_ALERT).text
        except TimeoutException:
            return None