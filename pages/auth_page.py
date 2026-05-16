import allure

from pages.base_page import BasePage, WebDriver
from webstore_config.locators import AuthLocators as locators


class AuthPage(BasePage):
    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)

    @property
    @allure.step('Запрос заголовка страницы "Авторизация"')
    def header(self) -> str:
        return self.find_visible_element(locators.HEADER).text

    def enter_login(self, login: str) -> None:
        with allure.step(f'Ввод логина: "{login}"'):
            self.find_visible_element(locators.LOGIN).send_keys(login)

    def enter_password(self, password: str) -> None:
        with allure.step(f'Ввод пароля: "{password}"'):
            self.find_visible_element(locators.PASSWORD).send_keys(password)

    @allure.step('Нажатие кнопки "Войти"')
    def click_login_button(self) -> None:
        self.find_clickable_element(locators.LOGIN_BUTTON).click()

    def log_in(self, login: str, password: str) -> None:
        self.enter_login(login)
        self.enter_password(password)
        self.click_login_button()