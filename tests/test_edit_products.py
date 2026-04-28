import allure

from pytest import mark
from pages.create_product_page import CreateProductPage
from pages.update_product_page import UpdateProductPage
from pages.edit_products_page import EditProductsPage
from tests.test_data.pages_data import CreateProductData, UpdateProductData


class TestEditProductsPage:
    @classmethod
    def setup_class(cls):
        cls.edit_products = EditProductsPage(cls.driver)
        cls.create_product = CreateProductPage(cls.driver)
        cls.update_product = UpdateProductPage(cls.driver)

    @allure.feature('NAVIGATION')
    @allure.story('Проверка перехода на страницу создания нового товара')
    def test_navigate_to_create_product(self, auth_by_admin):
        self.edit_products.open()
        self.edit_products.click_create_product_button()

        self.create_product.check_url()
        self.create_product.check_header(CreateProductData.HEADER)

    @allure.feature('NAVIGATION')
    @allure.story('Проверка перехода на страницу редактирования товара')
    @mark.parametrize('test_product', ['margarita'], indirect=True)
    def test_navigate_to_update_product_page(
            self,
            test_product,
            auth_by_admin
    ):
        self.edit_products.open()
        self.edit_products.click_edit_product_button(test_product.name)

        self.update_product.check_url()
        self.update_product.check_header(UpdateProductData.HEADER)

    @allure.feature('DELETE PRODUCT')
    @allure.story('Проверка удаления товара из каталога')
    @mark.parametrize('test_product', ['pepperoni'], indirect=True)
    def test_delete_product(
            self,
            test_product,
            auth_by_admin,
            delete_new_products
    ):
        self.edit_products.open()
        self.edit_products.click_delete_product_button(
            test_product.name
        )
        #EXPECTED_VALUE
        self.edit_products.check_existence_of_product(
            test_product.name,
            False
        )