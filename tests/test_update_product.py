import time
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
        self.update_product = UpdateProductPage(self.driver)

    def create_test_product(self):
        self.create_product.open()
        self.create_product.enter_product_name(product_data.MARGARITA_NAME)
        self.create_product.enter_product_description(product_data.MARGARITA_DESCRIPTION)
        self.create_product.enter_expected_category(product_data.MARGARITA_CATEGORY)
        self.create_product.enter_price_of_product(product_data.MARGARITA_PRICE_INT)
        self.create_product.enter_image_source(product_data.MARGARITA_IMAGE_URL)
        self.create_product.click_create_product_button()

    @allure.feature('NAVIGATION')
    @allure.story('Проверка перехода на страницу "Редактировать товар"')
    def test_navigate_to_edit_product_page(self, auth_by_admin):
        self.edit_products.open()

        if not self.edit_products.product_is_exists(product_data.MARGARITA_NAME):
            self.create_test_product()

        self.edit_products.click_edit_product_button(product_data.MARGARITA_NAME)

        self.update_product.check_url()
        self.update_product.check_header(headers.UPDATE_PRODUCT_PAGE)

    @allure.feature('UPDATE PRODUCT')
    @allure.story('Проверка редактирования поля "Наименование"')
    def test_edit_name_of_product(self, auth_by_admin):
        self.edit_products.open()

        if not self.edit_products.product_is_exists(product_data.MARGARITA_NAME):
            self.create_test_product()

        self.edit_products.click_edit_product_button(product_data.MARGARITA_NAME)
        self.update_product.enter_product_name(product_data.NEW_MARGARITA_NAME)
        self.update_product.click_update_product_button()

        time.sleep(0.3)
        self.edit_products.check_url()
        self.edit_products.check_header(headers.EDIT_PRODUCTS_PAGE)
        self.edit_products.check_product_is_exists(
            product_data.NEW_MARGARITA_NAME,
            True
        )

    @allure.feature('UPDATE PRODUCT')
    @allure.story('Проверка редактирования поля "Описание"')
    def test_edit_description_of_product(self, auth_by_admin):
        self.edit_products.open()

        if not self.edit_products.product_is_exists(product_data.MARGARITA_NAME):
            self.create_test_product()

        self.edit_products.click_edit_product_button(product_data.MARGARITA_NAME)
        self.update_product.enter_product_description(
            product_data.NEW_MARGARITA_DESCRIPTION
        )
        self.update_product.click_update_product_button()

        time.sleep(0.3)
        self.edit_products.check_url()
        self.edit_products.check_header(headers.EDIT_PRODUCTS_PAGE)
        self.edit_products.check_product_description(
            product_data.MARGARITA_NAME,
            product_data.NEW_MARGARITA_DESCRIPTION
        )

    @allure.feature('UPDATE PRODUCT')
    @allure.story('Проверка редактирования поля "Цена"')
    def test_edit_price_of_product(self, auth_by_admin):
        self.edit_products.open()

        if not self.edit_products.product_is_exists(
                product_data.MARGARITA_NAME
        ):
            self.create_test_product()

        self.edit_products.click_edit_product_button(
            product_data.MARGARITA_NAME
        )
        self.update_product.enter_price_of_product(
            product_data.NEW_MARGARITA_PRICE_INT
        )
        self.update_product.click_update_product_button()

        time.sleep(0.3)
        self.edit_products.check_url()
        self.edit_products.check_header(headers.EDIT_PRODUCTS_PAGE)
        self.edit_products.check_price_of_product(
            product_data.MARGARITA_NAME,
            product_data.NEW_MARGARITA_PRICE_STR
        )

    @allure.feature('UPDATE PRODUCT')
    @allure.story('Проверка редактирования поля "URL картинки"')
    def test_edit_image_source_of_product(self, auth_by_admin):
        self.edit_products.open()

        if not self.edit_products.product_is_exists(
                product_data.MARGARITA_NAME
        ):
            self.create_test_product()

        self.edit_products.click_edit_product_button(
            product_data.MARGARITA_NAME
        )

        # ЧАСТЬ ВЫШЕ, повторяется, почти, во всех тестах.

        self.update_product.enter_image_source(
            product_data.NEW_MARGARITA_IMAGE_URL
        )
        self.update_product.click_update_product_button()

        time.sleep(0.3)
        self.edit_products.check_url()
        self.edit_products.check_header(headers.EDIT_PRODUCTS_PAGE)
        self.edit_products.check_image_source_of_product(
            product_data.MARGARITA_NAME,
            product_data.NEW_MARGARITA_IMAGE_URL
        )

    @allure.feature('NAVIGATION')
    @allure.story('Проверка перехода на страницу "Редактирование товаров"')
    def test_navigation_to_edit_products_page(self, auth_by_admin):
        self.edit_products.open()

        if not self.edit_products.product_is_exists(
                product_data.MARGARITA_NAME
        ):
            self.create_test_product()

        self.edit_products.click_edit_product_button(
            product_data.MARGARITA_NAME
        )

        self.update_product.click_back_to_edit_products_page_button()

        time.sleep(0.3)
        self.edit_products.check_url()
        self.edit_products.check_header(headers.EDIT_PRODUCTS_PAGE)




