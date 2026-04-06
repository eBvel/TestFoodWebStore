import allure
import pytest

from pages.create_product_page import CreateProductPage
from tests.test_data import headers, product_data
from pages.edit_products_page import EditProductsPage


@pytest.mark.parametrize('driver', ['CHROME', 'FIREFOX'], indirect=True)
class TestCreateProductPage:
    def setup_method(self):
        self.edit_products = EditProductsPage(self.driver)
        self.create_product = CreateProductPage(self.driver)

    def _filling_product_data(
            self,
            name,
            description,
            category,
            price,
            image_url
    ):
        self.create_product.enter_product_name(name)
        self.create_product.enter_product_description(description)
        self.create_product.enter_expected_category(category)
        self.create_product.enter_price_of_product(price)
        self.create_product.enter_image_source(image_url)

    @allure.feature('CREATE PRODUCT')
    @allure.story('Проверка создания товара с корректными данными')
    def test_create_product(self, auth_by_admin):
        self.edit_products.open()

        #Если товар, который добавляем, уже существует - удаляем его
        if self.edit_products.product_is_exists(product_data.PEPPERONI_NAME):
            self.edit_products.click_delete_product_button(product_data.PEPPERONI_NAME)

        self.create_product.open()
        self._filling_product_data(
            product_data.PEPPERONI_NAME,
            product_data.PEPPERONI_DESCRIPTION,
            product_data.PEPPERONI_CATEGORY,
            product_data.PEPPERONI_PRICE_INT,
            product_data.PEPPERONI_IMAGE_URL
        )
        self.create_product.click_create_product_button()

        #Проверяем, что вернулись на страницу "Редактирование товаров"
        self.edit_products.check_url()
        self.edit_products.check_header(headers.EDIT_PRODUCTS_PAGE)
        #Проверяем наличие товара в каталоге
        self.edit_products.check_product_is_exists(
            product_data.PEPPERONI_NAME,
            True
        )

    @allure.feature('INCORRECT CREATE PRODUCT')
    @allure.story('Проверка создания товара с пустым полем "Имя"')
    def test_create_product_without_name(self, auth_by_admin):
        self.create_product.open()

        self._filling_product_data(
            '',
            product_data.PEPPERONI_DESCRIPTION,
            product_data.PEPPERONI_CATEGORY,
            product_data.PEPPERONI_PRICE_INT,
            product_data.PEPPERONI_IMAGE_URL
        )

        self.create_product.check_field_border_color(
            'name',
            'rgb(220, 53, 69)'
        )
        self.create_product.check_create_button_is_enabled(False)

    @allure.feature('INCORRECT CREATE PRODUCT')
    @allure.story('Проверка создания товара с пустым полем "Описание"')
    def test_create_product_without_description(self, auth_by_admin):
        self.create_product.open()

        self._filling_product_data(
            product_data.PEPPERONI_NAME,
            '',
            product_data.PEPPERONI_CATEGORY,
            product_data.PEPPERONI_PRICE_INT,
            product_data.PEPPERONI_IMAGE_URL
        )

        self.create_product.check_field_border_color(
            'description',
            'rgb(220, 53, 69)'
        )
        self.create_product.check_create_button_is_enabled(False)

    @allure.feature('INCORRECT CREATE PRODUCT')
    @allure.story('Проверка создания товара с пустым полем "URL картинки"')
    def test_create_product_without_image_url(self, auth_by_admin):
        self.create_product.open()

        self._filling_product_data(
            product_data.PEPPERONI_NAME,
            product_data.PEPPERONI_DESCRIPTION,
            product_data.PEPPERONI_CATEGORY,
            product_data.PEPPERONI_PRICE_INT,
            ''
        )

        self.create_product.check_field_border_color(
            'image_url',
            'rgb(220, 53, 69)'
        )
        self.create_product.check_create_button_is_enabled(False)

    @allure.feature('INCORRECT CREATE PRODUCT')
    @allure.story('Проверка создания товара с пустым полем "Цена"')
    def test_create_product_without_price(self, auth_by_admin):
        self.create_product.open()

        self._filling_product_data(
            product_data.PEPPERONI_NAME,
            product_data.PEPPERONI_DESCRIPTION,
            product_data.PEPPERONI_CATEGORY,
            '',
            product_data.PEPPERONI_IMAGE_URL
        )

        self.create_product.check_field_border_color(
            'price',
            'rgb(220, 53, 69)'
        )
        self.create_product.check_create_button_is_enabled(False)

    @allure.feature('CREATE PRODUCT')
    @allure.story('Проверка создания товара с нулевой ценой')
    def test_create_product_with_zero_price(self, auth_by_admin):
        self.edit_products.open()

        if self.edit_products.product_is_exists(product_data.MARGARITA_NAME):
            self.edit_products.click_delete_product_button(product_data.MARGARITA_NAME)

        self.create_product.open()
        self._filling_product_data(
            product_data.MARGARITA_NAME,
            product_data.MARGARITA_DESCRIPTION,
            product_data.MARGARITA_CATEGORY,
            0,
            product_data.MARGARITA_IMAGE_URL
        )
        self.create_product.click_create_product_button()

        self.edit_products.check_url()
        self.edit_products.check_header(headers.EDIT_PRODUCTS_PAGE)
        self.edit_products.check_product_is_exists(
            product_data.MARGARITA_NAME,
            True
        )

    @allure.feature('INCORRECT CREATE PRODUCT')
    @allure.story('Проверка создания товара с отрицательной ценой')
    def test_create_product_with_negative_price(self, auth_by_admin):
        self.create_product.open()

        self._filling_product_data(
            product_data.MARGARITA_NAME,
            product_data.MARGARITA_DESCRIPTION,
            product_data.MARGARITA_CATEGORY,
            -10,
            product_data.MARGARITA_IMAGE_URL
        )

        self.create_product.check_field_border_color(
            'price',
            'rgb(220, 53, 69)'
        )
        self.create_product.check_create_button_is_enabled(False)

    @allure.feature('NAVIGATION')
    @allure.story('Проверка перехода на страницу "Редактировать товары"')
    def test_navigation_to_edit_products_page(self, auth_by_admin):
        self.create_product.open()
        self.create_product.click_back_to_edit_products_page_button()

        self.edit_products.check_url()
        self.edit_products.check_header(headers.EDIT_PRODUCTS_PAGE)