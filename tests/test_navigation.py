import allure

from pages.cart_page import CartPage
from pages.catalog_page import CatalogPage
from pages.edit_products_page import EditProductsPage
from pages.navigation_bar_page import NavigationBarPage
from tests.test_data import headers


class TestNavigation:
    @classmethod
    def setup_class(cls):
        cls.navigation_bar = NavigationBarPage(cls.driver)
        cls.catalog = CatalogPage(cls.driver)
        cls.cart = CartPage(cls.driver)
        cls.edit_products = EditProductsPage(cls.driver)

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

    @allure.feature('NAVIGATION')
    @allure.story('Проверка перехода на страницу "Редактировать товары"')
    def test_navigate_to_edit_page(self, auth_by_admin):
        self.navigation_bar.click_navigation_bar()
        self.navigation_bar.click_edit_products_button()

        self.edit_products.check_url()
        self.edit_products.check_header(headers.EDIT_PRODUCTS_PAGE)

    @allure.feature('CLICK ON MENU ITEMS')
    @allure.story('Проверка выхода из учетной записи покупателя')
    def test_log_out(self, auth_by_user1):
        self.navigation_bar.open()
        self.navigation_bar.click_navigation_bar()
        self.navigation_bar.click_log_out()
        auth_by_user1.check_url()
        auth_by_user1.check_header(headers.AUTH_PAGE)