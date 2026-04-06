import time
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager as FirefoxDriverManager

from pages.auth_page import AuthPage
from pages.navigation_bar_page import NavigationBarPage


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
def auth_by_user(request):
    auth_page = AuthPage(request.cls.driver)
    try:
        auth_page.open()
        if auth_page.header == 'Авторизация':
            auth_page.enter_login('покупатель')
            auth_page.enter_password('покупатель')
            auth_page.click_login_button()
            time.sleep(0.3)
    except Exception:
        pass
    yield auth_page

@pytest.fixture
def auth_by_admin(request):
    auth_page = AuthPage(request.cls.driver)
    try:
        auth_page.open()
        if auth_page.header == 'Авторизация':
            auth_page.enter_login('admin')
            auth_page.enter_password('admin')
            auth_page.click_login_button()
            time.sleep(0.3)
    except Exception:
        pass
    yield auth_page


# @pytest.fixture(autouse=True)
# def open(request):
#     if request.cls.__name__ == "TestCatalogPage":
#         request.cls.catalog.open()
#     elif request.cls.__name__ == "TestCartPage":
#         request.cls.cart.open()