import allure

from pytest import mark
from pages.cart_page import CartPage
from pages.catalog_page import CatalogPage
from pages.edit_products_page import EditProductsPage
from pages.navigation_bar_page import NavigationBarPage
from tests.test_data.pages_data import (NavigationData, CartData, CatalogData,
                                        EditProductsData, AuthData)
from utils.assertion import Assert


class TestNavigation:
    @classmethod
    def setup_class(cls):
        cls.navigation_bar = NavigationBarPage(cls.driver)
        cls.catalog = CatalogPage(cls.driver)
        cls.cart = CartPage(cls.driver)
        cls.edit_products = EditProductsPage(cls.driver)

    @allure.feature('NAVIGATION')
    @allure.story('Проверка открытия меню навигации по кнопке "Сэндвич"')
    @mark.smoke
    def test_open_navigation_menu(self, auth_by_user1):
        self.navigation_bar.open()
        self.navigation_bar.click_navigation_bar()

        Assert.check_header(self.navigation_bar, NavigationData.HEADER)

    @allure.feature('NAVIGATION')
    @allure.story('Проверка перехода по пункту меню "Корзинка"')
    @mark.smoke
    def test_navigate_to_cart(self, auth_by_user1):
        self.navigation_bar.open()
        self.navigation_bar.click_navigation_bar()
        self.navigation_bar.click_cart_button()

        Assert.check_url(self.cart)
        Assert.check_header(self.cart, CartData.HEADER)

    @allure.feature('NAVIGATION')
    @allure.story('Проверка перехода по пункту меню "Магазин"')
    @mark.smoke
    def test_navigate_to_catalog(self, auth_by_user1):
        self.navigation_bar.open()
        self.navigation_bar.click_navigation_bar()
        self.navigation_bar.click_catalog_button()

        Assert.check_url(self.catalog)
        Assert.check_header(self.catalog, CatalogData.HEADER)

    @allure.feature('NAVIGATION')
    @allure.story('Проверка перехода по пункту меню "Редактировать товары"')
    @mark.smoke
    def test_navigate_to_edit_page(self, auth_by_admin):
        self.navigation_bar.click_navigation_bar()
        self.navigation_bar.click_edit_products_button()

        Assert.check_url(self.edit_products)
        Assert.check_header(self.edit_products, EditProductsData.HEADER)

    @allure.feature('NAVIGATION')
    @allure.story('Проверка выхода из учетной записи покупателя')
    @mark.smoke
    def test_log_out(self, auth_by_user1):
        self.navigation_bar.open()
        self.navigation_bar.click_navigation_bar()
        self.navigation_bar.click_log_out()

        Assert.check_url(auth_by_user1)
        Assert.check_header(auth_by_user1, AuthData.HEADER)