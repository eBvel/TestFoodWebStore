import allure

from pytest import mark
from pages.create_product_page import CreateProductPage
from pages.edit_products_page import EditProductsPage
from tests.test_data.datasets import Datasets
from tests.test_data.pages_data import EditProductsData
from tests.test_data.expected_values import ExpectedValues as EV
from utils.assertion import Assert


class TestCreateProductPage:
    @classmethod
    def setup_class(cls):
        cls.edit_products = EditProductsPage(cls.driver)
        cls.create_product = CreateProductPage(cls.driver)

    @allure.feature('VALID DATA')
    @allure.story('Проверка создания товара с корректными данными')
    @mark.smoke
    @mark.parametrize(
        'product',
        Datasets.CREATE_PRODUCT_CORRECT_PRODUCTS,
        ids=Datasets.CREATE_PRODUCT_CORRECT_PRODUCTS_IDS
    )
    def test_create_product(
            self,
            product,
            auth_by_admin,
            delete_new_products
    ):
        self.create_product.open()
        self.create_product.filling_fields(product)
        self.create_product.click_create_product_button()

        Assert.check_url(self.edit_products)
        Assert.check_header(self.edit_products, EditProductsData.HEADER)
        Assert.compare_values(
            value_name='Product is exists',
            current_value=self.edit_products.is_product_exists(product.name),
            expected_value=EV.CREATE_PRODUCT_IS_EXIST
        )

    @allure.feature('INVALID DATA')
    @allure.story('Проверка создания товара с негативными данными')
    @mark.parametrize(
        'field_name, product',
        Datasets.CREATE_PRODUCT_INCORRECT_PRODUCTS,
        ids=Datasets.CREATE_PRODUCT_INCORRECT_PRODUCTS_IDS
    )
    def test_create_product_with_negative_data(
            self,
            field_name,
            product,
            auth_by_admin
    ):
        self.create_product.open()
        self.create_product.filling_fields(product)

        Assert.compare_values(
            value_name="Field's border color",
            current_value=self.create_product.get_field_border_color(
                field_name
            ),
            expected_value=EV.CREATE_ERROR_BORDER_COLOR
        )
        Assert.compare_values(
            value_name='Enable status of create button',
            current_value=self.create_product.is_create_button_enabled(),
            expected_value=EV.CREATE_BUTTON_IS_DISABLED
        )

    @allure.feature('NAVIGATION')
    @allure.story('Проверка перехода на страницу "Редактировать товары"')
    def test_navigation_to_edit_products_page(self, auth_by_admin):
        self.create_product.open()
        self.create_product.click_back_to_edit_products_page_button()

        Assert.check_url(self.edit_products)
        Assert.check_header(self.edit_products, EditProductsData.HEADER)
