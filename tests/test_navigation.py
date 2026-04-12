import allure

from pages.cart_page import CartPage
from pages.catalog_page import CatalogPage
from pages.navigation_bar_page import NavigationBarPage
from tests.test_data import headers


class TestNavigation:

    @classmethod
    def setup_class(cls):
        cls.navigation_bar = NavigationBarPage(cls.driver)
        cls.catalog = CatalogPage(cls.driver)
        cls.cart = CartPage(cls.driver)

    @allure.feature('NAVIGATION MENU')
    @allure.story('Проверка открытия меню навигации по кнопке "Сэндвич"')
    def test_open_navigation_menu(self, auth_by_user1):
        self.navigation_bar.open()
        self.navigation_bar.click_navigation_bar()
        self.navigation_bar.check_header(headers.NAVIGATE_PAGE)

    @allure.feature('CLICK ON MENU ITEMS')
    @allure.story('Проверка перехода по пункту меню "Корзинка"')
    def test_navigate_to_cart(self, auth_by_user1):
        self.navigation_bar.open()
        self.navigation_bar.click_navigation_bar()
        self.navigation_bar.click_cart_button()
        self.cart.check_url()
        self.cart.check_header(headers.CART_PAGE)

    @allure.feature('CLICK ON MENU ITEMS')
    @allure.story('Проверка перехода по пункту меню "Магазин"')
    def test_navigate_to_catalog(self, auth_by_user1):
        self.navigation_bar.open()
        self.navigation_bar.click_navigation_bar()
        self.navigation_bar.click_catalog_button()
        self.catalog.check_url()
        self.catalog.check_header(headers.CATALOG_PAGE)

    @allure.feature('CLICK ON MENU ITEMS')
    @allure.story('Проверка выхода из учетной записи покупателя')
    def test_log_out(self, auth_by_user1):
        self.navigation_bar.open()
        self.navigation_bar.click_navigation_bar()
        self.navigation_bar.click_log_out()
        auth_by_user1.check_url()
        auth_by_user1.check_header(headers.AUTH_PAGE)