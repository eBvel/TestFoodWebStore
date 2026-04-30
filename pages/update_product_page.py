import allure

from selenium.common import ElementClickInterceptedException
from pages.create_product_page import CreateProductPage
from utils.assertion import AssertValues
from webstore_config.links import Links
from webstore_config.locators import CreateProductLocators as locators


class UpdateProductPage(CreateProductPage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = Links.UPDATE_PRODUCT_PAGE_URL

    @property
    @allure.step('Запрос идентификатора продукта')
    def product_id(self):
        return (
            self
            .find_visible_element(locators.ID_FIELD)
            .get_attribute('value')
        )

    def clear_input(self, locator):
        with allure.step(f'Запрос отчистки поля с локатором: "{locators}"'):
            try:
                element = self.find_clickable_element(locator)
                element.click()
                element.clear()
            except ElementClickInterceptedException:
                self.find_visible_element(locator).clear()

    def enter_product_name(self, name):
        self.clear_input(locators.NAME_FIELD)
        super().enter_product_name(name)

    def enter_product_description(self, description):
        self.clear_input(locators.DESCRIPTION_FIELD)
        super().enter_product_description(description)

    def enter_price_of_product(self, price):
        self.clear_input(locators.PRICE_FIELD)
        super().enter_price_of_product(price)

    def enter_image_source(self, url):
        self.clear_input(locators.IMAGE_SOURCE_FIELD)
        super().enter_image_source(url)

    @allure.step('Нажатие кнопки "Обновить товар"')
    def click_update_product_button(self):
        self.click_create_product_button()

    def check_url(self):
        expected_url = self.url + self.product_id
        with allure.step(f'Проверка URL текущей страницы: "UpdateProductPage".'
                         f' Ожидаемое значение: "{expected_url}"'):
            AssertValues.compare_values(
                "UPDATE PRODUCT: Url",
                self.get_current_url(),
                expected_url
            )