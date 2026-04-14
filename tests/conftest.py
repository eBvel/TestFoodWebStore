import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager as FirefoxDriverManager

from pages.auth_page import AuthPage
from pages.navigation_bar_page import NavigationBarPage
from tests.test_data import auth_data
from webstore_config.create_test_products import ProductFactory
from requests import Session

from webstore_config.webstore_api import WebstoreAPI


def pytest_addoption(parser):
    parser.addoption(
        '--browser',
        action='store',
        default='chrome',
        help='Browser\'s type variable. Possible values: "chrome" or "firefox".'
    )


@pytest.fixture(scope='session')
def browser_type(request):
    return request.config.getoption('--browser').lower()


@pytest.fixture(scope='session')
def driver(browser_type):
    if browser_type == 'chrome':
        option = webdriver.ChromeOptions()
        option.page_load_strategy = 'normal'
        with webdriver.Chrome(
                options=option,
                service=ChromeService(ChromeDriverManager().install())
        ) as chrome_driver:
            yield chrome_driver
    elif browser_type == 'firefox':
        with webdriver.Firefox(
                service=FirefoxService(FirefoxDriverManager().install())
        ) as firefox_driver:
            yield firefox_driver
    else:
        raise pytest.UsageError('"--browser" - should be "chrome" or "firefox".')


@pytest.fixture(scope='session')
def api():
    with Session() as session:
        api = WebstoreAPI(session)
        api.auth_by_admin(auth_data.ADMIN_LOGIN, auth_data.ADMIN_PASSWORD)
        yield api


@pytest.fixture(scope='class', autouse=True)
def attach_driver(request, driver):
    request.cls.driver = driver


@pytest.fixture
def auth(driver):
    def _auth(login, password):
        auth_page = AuthPage(driver)
        auth_page.open()
        auth_page.log_in(login, password)
        auth_page.get_header_text()
        return auth_page
    return _auth


@pytest.fixture
def log_out(driver):
    yield
    try:
        nav_bar = NavigationBarPage(driver)
        nav_bar.click_navigation_bar()
        nav_bar.click_log_out()
    except Exception:
        pass


@pytest.fixture
def auth_by_user1(auth, log_out):
    yield auth(auth_data.USER1_LOGIN, auth_data.USER1_PASSWORD)


@pytest.fixture
def auth_by_admin(auth, log_out):
    yield auth(auth_data.ADMIN_LOGIN, auth_data.ADMIN_PASSWORD)


@pytest.fixture
def products(request):
    products = []
    for param in request.param:
        products.append(request.getfixturevalue(param))
    return products


@pytest.fixture(scope='session')
def sandwich(request, api):
    sandwich = ProductFactory.sandwich()
    id = api.create_product(sandwich.to_json())
    yield sandwich
    api.delete_product(id)


@pytest.fixture(scope='session')
def nuggets(api):
    nuggets = ProductFactory.nuggets()
    id = api.create_product(nuggets.to_json())
    yield nuggets
    api.delete_product(id)