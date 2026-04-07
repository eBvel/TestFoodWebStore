import allure
import pytest

from pages.auth_page import AuthPage
from pages.catalog_page import CatalogPage
from tests.test_data import auth_data, headers


@pytest.mark.parametrize('driver', ['CHROME', 'FIREFOX'], indirect=True)
class TestAuth:
    def setup_method(self):
        self.auth_page = AuthPage(self.driver)
        self.catalog = CatalogPage(self.driver)

    @allure.feature('VALID LOG IN')
    @allure.story('Проверка авторизации с корректными данными')
    @pytest.mark.parametrize(
        'login, password',
        auth_data.ALL_USERS_LOGIN_DATA,
        ids=auth_data.ALL_USERS_IDS
    )
    def test_login(self, login, password, log_out):
        self.auth_page.open()
        self.auth_page.enter_login(login)
        self.auth_page.enter_password(password)
        self.auth_page.click_login_button()
        self.catalog.check_header(headers.CATALOG_PAGE)

    @allure.feature('LOG IN WITHOUT')
    @allure.story('Проверка авторизации без логина')
    @pytest.mark.parametrize(
        'password',
        [auth_data.USER1_PASSWORD, auth_data.ADMIN_PASSWORD ],
        ids=auth_data.USER1_ADMIN_IDS
    )
    def test_login_without_login(self, password, log_out):
        self.auth_page.open()
        self.auth_page.enter_password(password)
        self.auth_page.click_login_button()
        self.auth_page.check_header(headers.AUTH_PAGE)

    @allure.feature('LOG IN WITHOUT')
    @allure.story('Проверка авторизации без пароля')
    @pytest.mark.parametrize(
        'login',
        [auth_data.USER1_LOGIN, auth_data.ADMIN_LOGIN],
        ids=auth_data.USER1_ADMIN_IDS
    )
    def test_login_without_password(self, login, log_out):
        self.auth_page.open()
        self.auth_page.enter_login(login)
        self.auth_page.click_login_button()
        self.auth_page.check_header(headers.AUTH_PAGE)

    @allure.feature('LOG IN INCORRECT DATA')
    @allure.story('Проверка авторизации с некорректным логином')
    @pytest.mark.parametrize(
        'incorrect_login, password',
        auth_data.INCORRECT_LOGINS_LIST,
        ids=auth_data.USER1_ADMIN_IDS
    )
    def test_login_with_incorrect_login(self, incorrect_login, password, log_out):
        self.auth_page.open()
        self.auth_page.enter_login(incorrect_login)
        self.auth_page.enter_password(password)
        self.auth_page.click_login_button()
        self.auth_page.check_header(headers.AUTH_PAGE)

    @allure.feature('LOG IN INCORRECT DATA')
    @allure.story('Проверка авторизации с некорректным паролем')
    @pytest.mark.parametrize(
        'login, incorrect_password',
        auth_data.INCORRECT_PASSWORDS_LIST,
        ids=auth_data.USER1_ADMIN_IDS
    )
    def test_login_with_incorrect_password(self, login, incorrect_password, log_out):
        self.auth_page.open()
        self.auth_page.enter_login(login)
        self.auth_page.enter_password(incorrect_password)
        self.auth_page.click_login_button()
        self.auth_page.check_header(headers.AUTH_PAGE)