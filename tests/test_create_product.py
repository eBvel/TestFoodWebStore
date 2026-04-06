import allure
import pytest

from pages.create_product_page import CreateProductPage
from pages.update_product_page import UpdateProductPage
from tests.test_data import headers, product_data
from pages.edit_products_page import EditProductsPage


@pytest.mark.parametrize('driver', ['CHROME', 'FIREFOX'], indirect=True)
class TestCreateProductPage:
    def setup_method(self):
        self.edit_products = EditProductsPage(self.driver)
        self.create_product = CreateProductPage(self.driver)

    @allure.feature('CREATE PRODUCT')
    @allure.story('Проверка создания товара с корректными данными')
    def test_create_product(self, auth_by_admin):
        self.create_product.open()

        self.create_product.enter_product_name(product_data.PEPPERONI_NAME)
        self.create_product.enter_product_description(product_data.PEPPERONI_DESCRIPTION)
        self.create_product.enter_expected_category(product_data.PEPPERONI_CATEGORY)
        self.create_product.enter_price_of_product(product_data.PEPPERONI_PRICE_INT)
        self.create_product.enter_image_source(product_data.PEPPERONI_IMAGE_URL)
        self.create_product.click_create_product_button()

        #Проверяем, что вернулись на страницу "Редактирование товаров"
        self.edit_products.check_url()
        self.edit_products.check_header(headers.EDIT_PRODUCTS_PAGE)
        #Проверяем наличие товара в каталоге
        self.edit_products.check_product_is_exists(
            product_data.PEPPERONI_NAME,
            True
        )
