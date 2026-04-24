import pytest

from selenium import webdriver
from selenium.webdriver.support.wait import TimeoutException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager as FirefoxDriverManager

from pages.auth_page import AuthPage
from pages.navigation_bar_page import NavigationBarPage
from tests.test_data import auth_data
from tests.test_data.test_products import ProductFactory
from requests import Session

from webstore_config.webstore_api import WebstoreAPI


TEST_PRODUCTS = {}


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
        with webdriver.Chrome(
                options=webdriver.ChromeOptions(),
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
        api.auth(auth_data.ADMIN_LOGIN, auth_data.ADMIN_PASSWORD)
        api.auth(auth_data.USER1_LOGIN, auth_data.USER1_PASSWORD)
        yield api


@pytest.fixture(scope='class', autouse=True)
def attach_driver(request, driver):
    request.cls.driver = driver


@pytest.fixture(scope='session')
def auth_page(driver):
    return AuthPage(driver)


@pytest.fixture(scope='session')
def nav_bar(driver):
    return NavigationBarPage(driver)


@pytest.fixture
def auth(auth_page):
    def _auth(login, password):
        try:
            auth_page.open()
            auth_page.log_in(login, password)
            auth_page.get_header_text()
            return auth_page
        except TimeoutException:
            print('The user is already authorized.')
            return auth_page
    return _auth


@pytest.fixture
def log_out(nav_bar):
    yield
    try:
        if nav_bar.is_close():
            nav_bar.click_navigation_bar()
        nav_bar.click_log_out()
    except TimeoutException:
        print(f"The logout has already been performed.")


@pytest.fixture
def auth_by_user1(auth, log_out):
    yield auth(auth_data.USER1_LOGIN, auth_data.USER1_PASSWORD)


@pytest.fixture
def auth_by_admin(auth, log_out):
    yield auth(auth_data.ADMIN_LOGIN, auth_data.ADMIN_PASSWORD)


@pytest.fixture
def product(request, create_product):
    try:
        return request.getfixturevalue(request.param)
    except Exception:
        return create_product(ProductFactory.create_product_by_type(request.param))


@pytest.fixture
def products(request):
    products = []
    for param in request.param:
        products.append(request.getfixturevalue(param))
    return products


@pytest.fixture(scope='session')
def create_product(api):
    def _create_product(test_product):
        product_id = api.by_admin().create_product(test_product.to_json())
        TEST_PRODUCTS[product_id] = test_product
        return test_product
    return _create_product


@pytest.fixture(scope='session')
def sandwich(create_product):
    return create_product(ProductFactory.sandwich())


@pytest.fixture(scope='session')
def nuggets(create_product):
    return create_product(ProductFactory.nuggets())


@pytest.fixture(scope='session')
def caviar(create_product):
    return create_product(ProductFactory.caviar())


@pytest.fixture(autouse=True)
def clear_cart(api):
    product_list = api.by_user().get_product_id_list()
    for product_data in product_list:
        api.remove_from_cart(
            product_data['productId'],
            product_data['quantity']
        )


@pytest.fixture(scope='session', autouse=True)
def delete_product_list(api):
    yield
    if len(TEST_PRODUCTS):
        api.by_admin()
        for id in TEST_PRODUCTS.keys():
            api.delete_product(id)


@pytest.fixture
def product_count_to_cart(api):
    def _add_product_to_cart(product, count):
        product_id = next(
            (key for key, value in TEST_PRODUCTS.items() if value == product),
            None
        )
        return api.by_user().add_to_cart(product_id, count)
    return _add_product_to_cart
