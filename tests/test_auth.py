import allure

from pytest import mark
from pages.auth_page import AuthPage
from pages.catalog_page import CatalogPage
from tests.test_data.datasets import Datasets
from tests.test_data.pages_data import AuthData, CatalogData
from tests.test_data.login_data import LoginData
from utils.assertion import Assert


class TestAuth:
    @classmethod
    def setup_class(cls):
        cls.auth_page = AuthPage(cls.driver)
        cls.catalog = CatalogPage(cls.driver)

    @allure.feature('VALID DATA')
    @allure.story('Проверка авторизации с корректными данными')
    @mark.smoke
    @mark.parametrize(
        'login, password',
        Datasets.ALL_USERS_LOGIN_DATA,
        ids=Datasets.ALL_USERS_IDS
    )
    def test_log_in(self, login, password, log_out):
        self.auth_page.open()
        self.auth_page.log_in(login, password)

        Assert.check_header(self.catalog, CatalogData.HEADER)

    @allure.feature('EMPTY FIELDS')
    @allure.story('Проверка авторизации без логина')
    @mark.parametrize(
        'password',
        [LoginData.USER1_PASSWORD, LoginData.ADMIN_PASSWORD],
        ids=Datasets.USER1_ADMIN_IDS
    )
    def test_log_in_without_login(self, password, log_out):
        self.auth_page.open()
        self.auth_page.enter_password(password)
        self.auth_page.click_login_button()

        Assert.check_header(self.auth_page, AuthData.HEADER)

    @allure.feature('EMPTY FIELDS')
    @allure.story('Проверка авторизации без пароля')
    @mark.parametrize(
        'login',
        [LoginData.USER1_LOGIN, LoginData.ADMIN_LOGIN],
        ids=Datasets.USER1_ADMIN_IDS
    )
    def test_log_in_without_password(self, login, log_out):
        self.auth_page.open()
        self.auth_page.enter_login(login)
        self.auth_page.click_login_button()

        Assert.check_header(self.auth_page, AuthData.HEADER)

    @allure.feature('INVALID DATA')
    @allure.story('Проверка авторизации с некорректным логином')
    @mark.parametrize(
        'incorrect_login, password',
        Datasets.INCORRECT_LOGINS_LIST,
        ids=Datasets.USER1_ADMIN_IDS
    )
    def test_log_in_with_incorrect_login(
            self,
            incorrect_login,
            password,
            log_out
    ):
        self.auth_page.open()
        self.auth_page.log_in(incorrect_login, password)

        Assert.check_header(self.auth_page, AuthData.HEADER)

    @allure.feature('INVALID DATA')
    @allure.story('Проверка авторизации с некорректным паролем')
    @mark.parametrize(
        'login, incorrect_password',
        Datasets.INCORRECT_PASSWORDS_LIST,
        ids=Datasets.USER1_ADMIN_IDS
    )
    def test_log_in_with_incorrect_password(
            self,
            login,
            incorrect_password,
            log_out
    ):
        self.auth_page.open()
        self.auth_page.log_in(login, incorrect_password)

        Assert.check_header(self.auth_page, AuthData.HEADER)