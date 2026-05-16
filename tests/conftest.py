import os
import allure
import pytest

from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support.wait import TimeoutException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.remote.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager as FirefoxDriverManager
from _pytest.fixtures import FixtureRequest

from pages.auth_page import AuthPage
from pages.navigation_bar_page import NavigationBarPage
from tests.test_data.login_data import LoginData
from tests.test_data.test_products import ProductFactory, Product
from requests import Session
from webstore_config.webstore_api import WebstoreAPI
from typing import Generator, Callable, Union, Any

AuthFuncType = Callable[[str, str], AuthPage]
CreateProductType = Callable[[Product], Product]
YieldNone = Generator[None, Any, None]
Options = Union[ChromeOptions, FirefoxOptions]


TEST_PRODUCTS: dict[int, Product] = {}


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        driver = item.cls.driver

        now = datetime.now()
        screenshot_path = f'screenshots\\{now.strftime("%Y-%m-%d")}\\'
        screenshot_name = f'ss_{item.name}_{now.strftime("%H-%M-%S")}.png'

        if not os.path.exists(screenshot_path):
            os.makedirs(screenshot_path)

        driver.save_screenshot(screenshot_path+screenshot_name)
        allure.attach.file(
            screenshot_path+screenshot_name,
            attachment_type=allure.attachment_type.PNG
        )


def pytest_addoption(parser):
    parser.addoption(
        '--browser',
        action='store',
        default='chrome',
        help='Browser\'s type variable. '
             'Possible values: "chrome" or "firefox".'
    )
    parser.addoption(
        '--headless',
        action='store_true',
        default=False,
        help='The mode, that can run browser without UI.'
    )
    parser.addoption(
        '--fullscreen',
        action='store_true',
        default=False,
        help='Enlarges the window. The window will fill the screen, without '
             'blocking the operating system’s own menus and toolbars.'
    )


@pytest.fixture(scope='session', autouse=True)
def fullscreen(request: FixtureRequest, driver: WebDriver) -> None:
    if request.config.getoption('--fullscreen'):
        driver.maximize_window()


@pytest.fixture(scope='session')
def browser_type(request: FixtureRequest) -> str:
    return request.config.getoption('--browser').lower()


@pytest.fixture(scope='session')
def browser_options(
        browser_type: str,
        request: FixtureRequest
) -> Options:
    if browser_type == 'chrome':
        options = webdriver.ChromeOptions()
    elif browser_type == 'firefox':
        options = webdriver.FirefoxOptions()
    else:
        raise pytest.UsageError(
            '"--browser" - should be "chrome" or "firefox".'
        )

    if request.config.getoption('--headless'):
        options.add_argument('--headless')

    return options


@pytest.fixture(scope='session')
def driver(
        browser_type: str,
        browser_options: Options
) -> Generator[WebDriver | WebDriver, Any, None]:
    if browser_type == 'chrome':
        with webdriver.Chrome(
                options=browser_options,
                service=ChromeService(ChromeDriverManager().install())
        ) as chrome_driver:
            yield chrome_driver
    elif browser_type == 'firefox':
        with webdriver.Firefox(
                options=browser_options,
                service=FirefoxService(FirefoxDriverManager().install())
        ) as firefox_driver:
            yield firefox_driver


@pytest.fixture(scope='session')
def api() -> Generator[WebstoreAPI, Any, None]:
    with Session() as session:
        api = WebstoreAPI(session)
        api.auth(LoginData.ADMIN_LOGIN, LoginData.ADMIN_PASSWORD)
        api.auth(LoginData.USER1_LOGIN, LoginData.USER1_PASSWORD)
        yield api


@pytest.fixture(scope='class', autouse=True)
def attach_driver(request: FixtureRequest, driver: WebDriver) -> None:
    request.cls.driver = driver


@pytest.fixture(scope='session')
def auth_page(driver: WebDriver) -> AuthPage:
    return AuthPage(driver)


@pytest.fixture(scope='session')
def nav_bar(driver: WebDriver) -> NavigationBarPage:
    return NavigationBarPage(driver)


@pytest.fixture
def auth(auth_page: AuthPage) -> AuthFuncType:
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
def log_out(nav_bar: NavigationBarPage) -> YieldNone:
    yield
    try:
        if nav_bar.is_close():
            nav_bar.click_navigation_bar()
        nav_bar.click_log_out()
    except TimeoutException:
        print(f"The logout has already been performed.")


@pytest.fixture
def auth_by_user1(
        auth: AuthFuncType,
        log_out: YieldNone
) -> Generator[AuthPage, Any, None]:
    yield auth(LoginData.USER1_LOGIN, LoginData.USER1_PASSWORD)


@pytest.fixture
def auth_by_admin(
        auth: AuthFuncType,
        log_out: YieldNone
) -> Generator[AuthPage, Any, None]:
    yield auth(LoginData.ADMIN_LOGIN, LoginData.ADMIN_PASSWORD)


@pytest.fixture
def test_product(
        request: FixtureRequest,
        create_product: CreateProductType
) -> Product:
    try:
        return request.getfixturevalue(request.param)
    except Exception:
        return create_product(
            ProductFactory.create_product_by_type(request.param)
        )


@pytest.fixture
def test_products(
        request: FixtureRequest,
        create_product: CreateProductType
) -> list[Product]:
    products = []
    for param in request.param:
        try:
            products.append(request.getfixturevalue(param))
        except Exception:
            products.append(
                create_product(ProductFactory.create_product_by_type(param))
            )
    return products


@pytest.fixture(scope='session')
def create_product(api: WebstoreAPI) -> CreateProductType:
    def _create_product(product):
        product_id = api.by_admin().create_product(product.to_json())
        TEST_PRODUCTS[product_id] = product
        return product
    return _create_product


@pytest.fixture(scope='session')
def sandwich(create_product: CreateProductType) -> Product:
    return create_product(ProductFactory.sandwich())


@pytest.fixture(scope='session')
def nuggets(create_product: CreateProductType) -> Product:
    return create_product(ProductFactory.nuggets())


@pytest.fixture(scope='session')
def caviar(create_product: CreateProductType) -> Product:
    return create_product(ProductFactory.caviar())


@pytest.fixture(scope='session')
def margarita(create_product: CreateProductType) -> Product:
    return create_product(ProductFactory.margarita())


@pytest.fixture(autouse=True)
def clear_cart(api: WebstoreAPI) -> None:
    product_list = api.by_user().get_product_id_list()
    for product in product_list:
        api.remove_from_cart(
            product['productId'],
            product['quantity']
        )


@pytest.fixture(scope='session', autouse=True)
def delete_test_products(api: WebstoreAPI) -> YieldNone:
    yield
    if len(TEST_PRODUCTS):
        api.by_admin()
        for id in TEST_PRODUCTS.keys():
            api.delete_product(id)


@pytest.fixture
def delete_new_products(api: WebstoreAPI) -> YieldNone:
    before = api.by_admin().get_products_list()
    yield
    after = api.by_admin().get_products_list()
    for product in after:
        if product not in before:
            api.delete_product(product.get('id'))


@pytest.fixture
def product_count_to_cart(api: WebstoreAPI) -> Callable[[Product, int], bool]:
    def _add_product_to_cart(product, count=1):
        product_id = next(
            (key for key, value in TEST_PRODUCTS.items() if value == product),
            None
        )
        return api.by_user().add_to_cart(product_id, count)
    return _add_product_to_cart
