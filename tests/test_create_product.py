import allure

from pytest import mark
from pages.create_product_page import CreateProductPage
from tests.test_data import headers
from pages.edit_products_page import EditProductsPage
from tests.test_data.test_products import ProductFactory


class TestCreateProductPage:
    @classmethod
    def setup_class(cls):
        cls.edit_products = EditProductsPage(cls.driver)
        cls.create_product = CreateProductPage(cls.driver)

    @allure.feature('CREATE PRODUCT')
    @allure.story('Проверка создания товара с корректными данными')
    @mark.parametrize(
        'product',
        [ProductFactory.pepperoni(), ProductFactory.pepperoni(price=0)],
        ids=['custom product', 'product with zero price']
    )
    def test_create_product(self, product, auth_by_admin, delete_new_products):
        self.create_product.open()
        self.create_product.filling_fields(product)
        self.create_product.click_create_product_button()

        #EXPECTED_VALUE
        self.edit_products.check_url()
        self.edit_products.check_header(headers.EDIT_PRODUCTS_PAGE)
        self.edit_products.check_existence_of_product(
            product.name,
            True
        )

    @allure.feature('INCORRECT CREATE PRODUCT')
    @allure.story('Проверка создания товара с пустым полем "Цена"')
    @mark.parametrize(
        'field_name, product',
        [
            ('name', ProductFactory.pepperoni(name='')),
            ('description', ProductFactory.pepperoni(description='')),
            ('price', ProductFactory.pepperoni(price=None)),
            ('price', ProductFactory.pepperoni(price=-1)),
            ('image_url', ProductFactory.pepperoni(image_url=''))
        ],
        ids=[
            'empty name',
            'empty description',
            'None price',
            'negative price',
            'empty image_url'
        ]
    )
    def test_create_product_with_negative_data(
            self,
            field_name,
            product,
            auth_by_admin
    ):
        self.create_product.open()
        self.create_product.filling_fields(product)

        self.create_product.check_field_border_color(
            field_name,
            'rgb(220, 53, 69)'
        )
        #EXPECTED_VALUE
        self.create_product.check_create_button_is_enabled(False)

    @allure.feature('NAVIGATION')
    @allure.story('Проверка перехода на страницу "Редактировать товары"')
    def test_navigation_to_edit_products_page(self, auth_by_admin):
        self.create_product.open()
        self.create_product.click_back_to_edit_products_page_button()

        self.edit_products.check_url()
        self.edit_products.check_header(headers.EDIT_PRODUCTS_PAGE)