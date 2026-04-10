import time
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager as FirefoxDriverManager

from pages.auth_page import AuthPage
from pages.navigation_bar_page import NavigationBarPage
from pages.base_page import BasePage
from tests.test_data import headers, auth_data


@pytest.fixture(scope='class', autouse=True)
def driver(request):
    if request.param == "CHROME":
        with webdriver.Chrome(
                options=webdriver.ChromeOptions(),
                service=ChromeService(ChromeDriverManager().install())
        ) as chrome_driver:
            request.cls.driver = chrome_driver
            yield
    elif request.param == "FIREFOX":
        with webdriver.Firefox(
                service=FirefoxService(FirefoxDriverManager().install())
        ) as firefox_driver:
            request.cls.driver = firefox_driver
            yield
    return None


@pytest.fixture
def log_out(request):
    try:
        nav_bar = NavigationBarPage(request.cls.driver)
        if nav_bar.get_header_text() == "Магазин":
            nav_bar.click_navigation_bar()
            nav_bar.click_log_out()
    except Exception:
        pass


@pytest.fixture
def auth_by_user(request, auth):
    yield auth(auth_data.USER1_LOGIN, auth_data.USER1_PASSWORD)

@pytest.fixture
def auth_by_admin(request, auth):
    yield auth(auth_data.ADMIN_LOGIN, auth_data.ADMIN_PASSWORD)

@pytest.fixture
def auth(request, is_auth):
    def _auth(login, password):
        auth_page = AuthPage(request.cls.driver)

        if not is_auth:
            auth_page.open()
            auth_page.enter_login(login)
            auth_page.enter_password(password)
            auth_page.click_login_button()
            time.sleep(0.3)

    yield _auth

@pytest.fixture
def is_auth(request):
    base_page = BasePage(request.cls.driver)
    header = base_page.header

    return header in headers.main


# @pytest.fixture(autouse=True)
# def open(request):
#     if request.cls.__name__ == "TestCatalogPage":
#         request.cls.catalog.open()
#     elif request.cls.__name__ == "TestCartPage":
#         request.cls.cart.open()