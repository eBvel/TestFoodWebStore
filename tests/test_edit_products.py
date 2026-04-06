import time
import allure
import pytest

from pages.create_product_page import CreateProductPage
from pages.navigation_bar_page import NavigationBarPage
from pages.update_product_page import UpdateProductPage
from tests.test_data import headers, product_data
from pages.edit_products_page import EditProductsPage

@pytest.mark.parametrize('driver', ['CHROME', 'FIREFOX'], indirect=True)
class TestEditProductsPage:
    def setup_method(self):
        self.edit_products = EditProductsPage(self.driver)
        self.navigation_bar = NavigationBarPage(self.driver)
        self.create_product = CreateProductPage(self.driver)
        self.update_product = UpdateProductPage(self.driver)

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
    def test_navigate_to_update_product_page(self, auth_by_admin):
        self.edit_products.open()
        self.edit_products.click_edit_product_button(product_data.NAME)

        self.update_product.check_url()
        self.update_product.check_header(headers.UPDATE_PRODUCT_PAGE)

    @allure.feature('DELETE PRODUCT')
    @allure.story('Проверка удаления товара из каталога')
    def test_delete_product(self, auth_by_admin):
        self.edit_products.open()

        #Проверяем существует ли товар в каталоге. Если нет, то создаем его.
        if not self.edit_products.product_is_exists(
                product_data.MARGARITA_NAME
        ):
            self.create_product.open()
            self.create_product.enter_product_name(
                product_data.MARGARITA_NAME
            )
            self.create_product.enter_product_description(
                product_data.MARGARITA_DESCRIPTION
            )
            self.create_product.enter_expected_category(
                product_data.MARGARITA_CATEGORY
            )
            self.create_product.enter_price_of_product(
                product_data.MARGARITA_PRICE_INT
            )
            self.create_product.enter_image_source(
                product_data.MARGARITA_IMAGE_URL
            )
            self.create_product.click_create_product_button()

        #Удаление товара
        self.edit_products.click_delete_product_button(
            product_data.MARGARITA_NAME
        )

        #Проверка, что товар отсутствует в списке.
        time.sleep(0.3)
        self.edit_products.check_product_is_exists(
            product_data.MARGARITA_NAME,
            False
        )


