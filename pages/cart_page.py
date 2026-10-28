import allure

from selenium.common import TimeoutException
from pages.base_page import BasePage, WebDriver
from webstore_config.links import Links
from webstore_config.locators import CartLocators as locators, LocatorType


class CartPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.url = Links.CART_PAGE_URL

    @allure.step('Запрос текста "сообщения" о пустой корзине')
    def get_empty_text(self) -> str:
        return self.find_visible_element(locators.CART_IS_EMPTY_TEXT).text

    @allure.step('Запрос, пустая корзина или нет')
    def is_empty(self) -> bool:
        try:
            self.find_visible_element(locators.CART_IS_EMPTY_TEXT)
            return True
        except TimeoutException:
            return False

    @allure.step('Запрос, отображается поле "итоговая стоимость" '
                 'в корзине или нет')
    def is_total_cost_displayed(self) -> bool:
        return self.find_visible_element(locators.TOTAL_COST).is_displayed()

    @allure.step('Запрос, отображается кнопка "Оформить заказ" или нет')
    def is_place_an_order_button_display(self) -> bool:
        try:
            return (
                self
                .find_visible_element(locators.PLACE_AN_ORDER_BUTTON)
                .is_displayed()
            )
        except TimeoutException:
            return False

    def get_product_price(self, product_name: str) -> str:
        with allure.step(f'Запрос "цены" товара "{product_name}" в корзине'):
            return (
                self
                .find_visible_element(locators.PRODUCT_PRICE(product_name))
                .text
            )

    def multiple_button_click(
            self,
            product_name: str,
            locator: LocatorType,
            click_count: int = 1
    ) -> None:
        for i in range(click_count):
            self.click(locator)
            self.is_attribute_present(
                locators.COUNT_OF_PRODUCT(product_name),
                'value',
                str(i+1)
            )

    def add_product(self, product_name: str, count: int = 1) -> None:
        with allure.step(f'Добавление товара "{product_name}" '
                         f'в количестве "{count}" в корзинку'):
            self.multiple_button_click(
                product_name,
                locators.ADD_BUTTON(product_name),
                count
            )

    def remove_product(self, product_name: str, count: int = 1) -> None:
        with allure.step(f'Удаление товара "{product_name}"'
                         f'в количестве "{count}" из корзинки'):
            self.multiple_button_click(
                product_name,
                locators.REMOVE_BUTTON(product_name),
                count
            )

    def get_product_count(self, product_name: str) -> int:
        with allure.step(f'Запрос кол-ва товара "{product_name}" в корзинке'):
            self.wait_value_change(locators.COUNT_OF_PRODUCT(product_name))
            return int(
                self
               .find_visible_element(locators.COUNT_OF_PRODUCT(product_name))
               .get_attribute('value')
            )

    @allure.step('Запрос "итоговой стоимости" товаров в корзине')
    def get_total_cost(self) -> str:
        return self.find_visible_element(locators.TOTAL_COST).text

    @allure.step('Нажатие кнопки "Оформить заказ"')
    def click_place_an_order_button(self) -> None:
        self.click(locators.PLACE_AN_ORDER_BUTTON)