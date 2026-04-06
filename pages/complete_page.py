import allure

from pages.base_page import BasePage
from webstore_config.links import Links
from webstore_config.locators import CompleteLocators as locators
from utils.assertion import AssertValues


class CompletePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = Links.COMPLETE_PAGE_URL

    @property
    @allure.step("Запрос заголовка страницы завершения заказа")
    def header(self):
        return self.find_visible_element(locators.HEADER).text

    @allure.step("Запрос сообщения об успешно созданном заказе")
    def get_complete_message(self):
        return self.find_visible_element(locators.COMPLETE_MESSAGE).text

    @allure.step('Нажатие кнопки "Вернутся в магазин"')
    def click_back_to_catalog_button(self):
        self.find_clickable_element(locators.BACK_TO_CATALOG_BUTTON).click()

    def check_complete_message(self, expected_value):
        with allure.step(f'Проверка сообщения об успешно созданном заказе. '
                         f'Ожидаемое значение: "{expected_value}"'):
            AssertValues.compare_values(
                "COMPLETE: COMPLETE MESSAGE",
                self.get_complete_message(),
                expected_value
            )