import time
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager as FirefoxDriverManager

from pages.auth_page import AuthPage
from pages.create_product_page import CreateProductPage
from pages.edit_products_page import EditProductsPage
from pages.navigation_bar_page import NavigationBarPage
from pages.base_page import BasePage
from tests.test_data import headers, auth_data, product_data


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


@pytest.fixture(scope='class', autouse=True)
def attach_driver(request, driver):
    request.cls.driver = driver


@pytest.fixture
def log_out(driver):
    try:
        nav_bar = NavigationBarPage(driver)
        if nav_bar.get_header_text() == "Магазин":
            nav_bar.click_navigation_bar()
            nav_bar.click_log_out()
    except Exception:
        pass


@pytest.fixture
def auth_by_user1(auth):
    return auth(auth_data.USER1_LOGIN, auth_data.USER1_PASSWORD)


@pytest.fixture
def auth_by_admin(auth):
    return auth(auth_data.ADMIN_LOGIN, auth_data.ADMIN_PASSWORD)


@pytest.fixture
def auth(driver, is_auth):
    def _auth(login, password):
        auth_page = AuthPage(driver)

        if not is_auth:
            auth_page.open()
            auth_page.enter_login(login)
            auth_page.enter_password(password)
            auth_page.click_login_button()
            # explicit wait something. For example, wait to load a header of page.
            time.sleep(0.3)

        return auth_page
    return _auth


@pytest.fixture
def is_auth(driver):
    return BasePage(driver).header in headers.main


# @pytest.fixture(scope='class', autouse=False)
# def test_data(request, auth_by_admin, create_product):
#     edit_page = EditProductsPage(request.cls.driver)
#     edit_page.open()
#
#     if not edit_page.product_is_exists(product_data.SANDWICH_NAME):
#         edit_page.click_create_product_button()
#         create_product(
#             product_data.SANDWICH_NAME,
#             product_data.SANDWICH_DESCRIPTION,
#             product_data.SANDWICH_CATEGORY,
#             product_data.SANDWICH_PRICE_INT,
#             product_data.SANDWICH_IMAGE_URL
#         )
#     if not edit_page.product_is_exists(product_data.CAVIAR_NAME):
#         edit_page.click_create_product_button()
#         create_product(
#             product_data.CAVIAR_NAME,
#             product_data.CAVIAR_DESCRIPTION,
#             product_data.CAVIAR_CATEGORY,
#             product_data.CAVIAR_PRICE_INT,
#             product_data.CAVIAR_IMAGE_URL
#         )
#
#
#
# @pytest.fixture
# def create_product(request):
#     def _create(name, description, category, price, image_url):
#         create_product = CreateProductPage(request.cls.driver)
#         create_product.enter_product_name(name)
#         create_product.enter_product_description(description)
#         create_product.enter_expected_category(category)
#         create_product.enter_price_of_product(price)
#         create_product.enter_image_source(image_url)
#         create_product.click_create_product_button()
#     return _create