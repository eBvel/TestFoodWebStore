import allure

from pytest import mark
from pages.create_product_page import CreateProductPage
from pages.navigation_bar_page import NavigationBarPage
from pages.update_product_page import UpdateProductPage
from tests.test_data import headers
from pages.edit_products_page import EditProductsPage


class TestEditProductsPage:
    @classmethod
    def setup_class(cls):
        cls.edit_products = EditProductsPage(cls.driver)
        cls.navigation_bar = NavigationBarPage(cls.driver)
        cls.create_product = CreateProductPage(cls.driver)
        cls.update_product = UpdateProductPage(cls.driver)

#Move test to test_navigation
    @allure.feature('NAVIGATION')
    @allure.story('Проверка перехода на страницу "Редактировать товары"')
    def test_navigate_to_edit_page(self, auth_by_admin):
        self.navigation_bar.click_navigation_bar()
        self.navigation_bar.click_edit_products_button()

        self.edit_products.check_url()
        self.edit_products.check_header(headers.EDIT_PRODUCTS_PAGE)

    @allure.feature('NAVIGATION')
    @allure.story('Проверка перехода на страницу создания нового товара')
    def test_navigate_to_create_product(self, auth_by_admin):
        self.edit_products.open()
        self.edit_products.click_create_product_button()

        self.create_product.check_url()
        self.create_product.check_header(headers.CREATE_PRODUCT_PAGE)

    @allure.feature('NAVIGATION')
    @allure.story('Проверка перехода на страницу редактирования товара')
    @mark.parametrize('product', ['margarita'], indirect=True)
    def test_navigate_to_update_product_page(self, product, auth_by_admin):
        self.edit_products.open()
        self.edit_products.click_edit_product_button(product.name)

        self.update_product.check_url()
        self.update_product.check_header(headers.UPDATE_PRODUCT_PAGE)

    @allure.feature('DELETE PRODUCT')
    @allure.story('Проверка удаления товара из каталога')
    @mark.parametrize('product', ['margarita'], indirect=True)
    def test_delete_product(self, product, auth_by_admin):
        self.edit_products.open()
        self.edit_products.click_delete_product_button(
            product.name
        )
        self.edit_products.check_product_was_removed(
            product.name,
            True
        )