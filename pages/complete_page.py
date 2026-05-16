import allure

from pages.base_page import BasePage, WebDriver
from webstore_config.links import Links
from webstore_config.locators import CompleteLocators as locators


class CompletePage(BasePage):
    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
        self.url = Links.COMPLETE_PAGE_URL

    @allure.step("Запрос сообщения об успешно созданном заказе")
    def get_complete_message(self) -> str:
        return self.find_visible_element(locators.COMPLETE_MESSAGE).text

    @allure.step('Нажатие кнопки "Вернутся в магазин"')
    def click_back_to_catalog_button(self) -> None:
        self.click(locators.BACK_TO_CATALOG_BUTTON)