import allure

from pytest import mark
from pages.create_product_page import CreateProductPage
from pages.update_product_page import UpdateProductPage
from pages.edit_products_page import EditProductsPage
from tests.test_data.pages_data import CreateProductData, UpdateProductData
from tests.test_data.expected_values import ExpectedValues as EV
from utils.assertion import Assert


class TestEditProductsPage:
    @classmethod
    def setup_class(cls):
        cls.edit_products = EditProductsPage(cls.driver)
        cls.create_product = CreateProductPage(cls.driver)
        cls.update_product = UpdateProductPage(cls.driver)

    @allure.feature('NAVIGATION')
    @allure.story('Проверка перехода на страницу создания нового товара')
    @mark.smoke
    def test_navigate_to_create_product(self, auth_by_admin):
        self.edit_products.open()
        self.edit_products.click_create_product_button()

        Assert.check_header(self.create_product, CreateProductData.HEADER)
        Assert.check_url(self.create_product)

    @allure.feature('NAVIGATION')
    @allure.story('Проверка перехода на страницу редактирования товара')
    @mark.smoke
    @mark.parametrize('test_product', ['margarita'], indirect=True)
    def test_navigate_to_update_product_page(
            self,
            test_product,
            auth_by_admin
    ):
        self.edit_products.open()
        self.edit_products.click_edit_product_button(test_product.name)

        Assert.check_header(self.update_product, UpdateProductData.HEADER)
        Assert.compare_values(
            value_name='UpdateProductPage - URL',
            current_value=self.update_product.get_current_url(),
            expected_value=self.update_product.get_url()
        )

    @allure.feature('FUNCTIONAL')
    @allure.story('Проверка удаления товара из каталога')
    @mark.smoke
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

        Assert.compare_values(
            value_name='Present is exists',
            current_value= self.edit_products.is_product_exists(
                test_product.name
            ),
            expected_value=EV.EDIT_PRODUCT_IS_NOT_EXIST
        )