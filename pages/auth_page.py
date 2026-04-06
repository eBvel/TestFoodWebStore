import allure
from pages.base_page import BasePage
from webstore_config.locators import AuthLocators as locators


class AuthPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @property
    @allure.step('Запрос заголовка страницы "Авторизация"')
    def header(self):
        return self.find_visible_element(locators.HEADER, 3).text

    def enter_login(self, login):
        with allure.step(f'Ввод логина: "{login}".'):
            self.find_visible_element(locators.LOGIN).send_keys(login)

    def enter_password(self, password):
        with allure.step(f'Ввод пароля: "{password}".'):
            self.find_visible_element(locators.PASSWORD).send_keys(password)

    @allure.step('Нажатие кнопки "Войти".')
    def click_login_button(self):
        self.find_clickable_element(locators.LOGIN_BUTTON).click()