import allure
from pages.base_page import BasePage
from utils.assertion import AssertValues
from webstore_config.links import Links
from webstore_config.locators import UserDataLocators as locators


class CheckoutPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = Links.PLACE_AN_ORDER_PAGE_URL

    @property
    @allure.step('Запрос заголовка страницы "Оформление заказа"')
    def header(self):
        return self.find_visible_element(locators.HEADER).text

    def enter_first_name(self, first_name):
        with allure.step(f'Заполнение имени значением "{first_name}"'):
            self.find_visible_element(locators.FIRST_NAME_FIELD).send_keys(first_name)

    def enter_second_name(self, second_name):
        with allure.step(f'Заполнение фамилии значением "{second_name}"'):
            self.find_visible_element(locators.SECOND_NAME_FIELD).send_keys(second_name)

    def enter_middle_name(self, middle_name):
        with allure.step(f'Заполнение отчества значением "{middle_name}"'):
            self.find_visible_element(locators.MIDDLE_NAME_FIELD).send_keys(middle_name)

    def enter_delivery_address(self, address):
        with allure.step(f'Заполнение адреса доставки значением "{address}"'):
            self.find_visible_element(locators.DELIVERY_ADDRESS_FIELD).send_keys(address)

    def enter_cart_number(self, cart_number):
        with allure.step(f'Заполнение номера карты значением "{cart_number}"'):
            self.find_visible_element(locators.CART_NUMBER_FIELD).send_keys(cart_number)

    @allure.step('Нажатие кнопки "Оформить заказ"')
    def click_place_an_order_button(self):
        self.find_visible_element(locators.PLACE_AN_ORDER_BUTTON).click()

    @allure.step('Нажатие кнопки "Обратно в магазин"')
    def click_back_to_catalog(self):
        self.find_clickable_element(locators.BACK_TO_CATALOG_BUTTON).click()

    @allure.step('Запрос значения из поля "Имя".')
    def get_first_name(self):
        return self.find_visible_element(locators.FIRST_NAME_FIELD).text

    @allure.step('Запрос значения из поля "Фамилия".')
    def get_second_name(self):
        return self.find_visible_element(locators.SECOND_NAME_FIELD).text

    @allure.step('Запрос значения из поля "Адрес доставки".')
    def get_delivery_address(self):
        return self.find_visible_element(locators.DELIVERY_ADDRESS_FIELD).text

    @allure.step('Запрос значения из поля "Номер карты".')
    def get_cart_number(self):
        return self.find_visible_element(locators.CART_NUMBER_FIELD).text

    @allure.step('Попытка получить текст уведомления о пустых полях')
    def try_get_empty_fields_alert(self):
        try:
            return self.find_visible_element(locators.EMPTY_FIELDS_ALERT).text
        except Exception:
            return None

    def check_empty_fields_alert(self, expected_value):
        with allure.step(f'Проверка текста уведомления о пустых полях. '
                         f'Ожидаемое значение: f"{expected_value}"'):
            AssertValues.compare_values(
                "EMPTY FIELDS ALERT",
                self.try_get_empty_fields_alert(),
                expected_value
            )

    def check_first_name(self, expected_value):
        with allure.step(f'Проверка поля "Имя". Ожидаемое значение: '
                         f'f"{expected_value}"'):
            AssertValues.compare_values(
                "FIRST NAME",
                self.get_first_name(),
                expected_value
            )

    def check_second_name(self, expected_value):
        with allure.step(f'Проверка поля "Фамилия". Ожидаемое значение: '
                         f'f"{expected_value}"'):
            AssertValues.compare_values(
                "SECOND_NAME",
                self.get_second_name(),
                expected_value
            )

    def check_cart_number(self, expected_value):
        with allure.step(f'Проверка поля "Номер карты". Ожидаемое значение: '
                         f'f"{expected_value}"'):
            AssertValues.compare_values(
                "CART_NUMBER",
                self.get_cart_number(),
                expected_value
            )