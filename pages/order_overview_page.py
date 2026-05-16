import allure

from pages.base_page import BasePage, WebDriver
from webstore_config.locators import OrderOverviewLocators as locators
from webstore_config.links import Links


class OrderOverviewPage(BasePage):
    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
        self.url =Links.ORDER_OVERVIEW_PAGE_URL

    @allure.step('Запрос списка товаров в заказе')
    def get_products_title(self) -> list[str]:
        return [
            product.text for product in self.find_elements(locators.PRODUCTS)
        ]

    def get_product_count(self, product_name: str) -> int:
        with allure.step(f'Запрос количества товара "{product_name}" '
                         f'в заказа'):
            return int(
                self
                .find_visible_element(locators.PRODUCT_DATA(product_name))
                .text
                .split(' ')[0]
            )

    def get_product_price(self, product_name: str) -> str:
        with allure.step(f'Запрос цены товара "{product_name}" в заказе'):
            return (
                self
                .find_visible_element(locators.PRODUCT_DATA(product_name))
                .text
                .split('по ')[1]
            )

    @allure.step('Запрос значения из поля "Имя" в заказе')
    def get_first_name(self) -> str:
        return (
            self
            .find_visible_element(locators.FIRST_NAME)
            .text
            .split(': ')[1]
        )

    @allure.step('Запрос значения из поля "Фамилия" в заказе')
    def get_second_name(self) -> str:
        return (
            self
            .find_visible_element(locators.SECOND_NAME)
            .text
            .split(': ')[1]
        )

    @allure.step('Запрос значения из поля "Отчество" в заказе')
    def get_middle_name(self) -> str:
        return (
            self
            .find_visible_element(locators.MIDDLE_NAME)
            .text
            .split(': ')[1]
        )

    @allure.step("Запрос данных об адресе доставки заказа")
    def get_delivery_address(self) -> str:
        return (
            self
            .find_visible_element(locators.DELIVERY_ADDRESS)
            .text
            .split(': ')[1]
        )

    @allure.step("Запрос данных об оплате заказа")
    def get_cart_number(self) -> str:
        return (
            self
            .find_visible_element(locators.CART_NUMBER)
            .text
            .split(': ')[1]
        )

    @allure.step("Запрос итоговой стоимости заказа")
    def get_total_cost(self) -> str:
        return (
            self
            .find_visible_element(locators.TOTAL_COST)
            .text
            .split(': ')[1]
        )

    @allure.step('Запрос "общего количества" товаров в заказе')
    def get_total_count(self) -> int:
        return int(
            self
            .find_visible_element(locators.TOTAL_COUNT)
            .text
            .split(': ')[1]
        )

    @allure.step('Нажатие кнопки "Завершить заказ"')
    def click_complete_order_button(self) -> None:
        self.click(locators.COMPLETE_ORDER_BUTTON)

    @allure.step('Нажатие кнопки "Обратно в магазин"')
    def click_back_to_catalog_button(self) -> None:
        self.click(locators.BACK_TO_CATALOG_BUTTON)