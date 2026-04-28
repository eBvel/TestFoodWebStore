import allure

from pytest import mark
from pages.create_product_page import CreateProductPage
from pages.update_product_page import UpdateProductPage
from tests.test_data import headers, product_data
from pages.edit_products_page import EditProductsPage


class TestCreateProductPage:
    @classmethod
    def setup_class(cls):
        cls.edit_products = EditProductsPage(cls.driver)
        cls.create_product = CreateProductPage(cls.driver)
        cls.update_product = UpdateProductPage(cls.driver)

    @allure.feature('NAVIGATION')
    @allure.story('Проверка перехода на страницу "Редактировать товар"')
    @mark.parametrize('test_product', ['margarita'], indirect=True)
    def test_navigate_to_edit_product_page(self, test_product, auth_by_admin):
        self.edit_products.open()
        self.edit_products.click_edit_product_button(test_product.name)

        self.update_product.check_url()
        self.update_product.check_header(headers.UPDATE_PRODUCT_PAGE)

    @allure.feature('UPDATE PRODUCT')
    @allure.story('Проверка редактирования поля "Наименование"')
    @mark.parametrize('test_product', ['pepperoni'], indirect=True)
    def test_edit_name_of_product(
            self,
            test_product,
            auth_by_admin,
            delete_new_products
    ):
        self.edit_products.open()
        self.edit_products.click_edit_product_button(test_product.name)
        self.update_product.enter_product_name(product_data.NEW_MARGARITA_NAME)
        self.update_product.click_update_product_button()

        self.edit_products.check_url()
        self.edit_products.check_header(headers.EDIT_PRODUCTS_PAGE)
        #EXPECTED_VALUE
        self.edit_products.check_existence_of_product(
            product_data.NEW_MARGARITA_NAME,
            True
        )

    @allure.feature('UPDATE PRODUCT')
    @allure.story('Проверка редактирования поля "Описание"')
    @mark.parametrize('test_product', ['margarita'], indirect=True)
    def test_edit_description_of_product(self, test_product, auth_by_admin):
        self.edit_products.open()
        self.edit_products.click_edit_product_button(test_product.name)
        self.update_product.enter_product_description(
            product_data.NEW_MARGARITA_DESCRIPTION
        )
        self.update_product.click_update_product_button()

        self.edit_products.check_url()
        self.edit_products.check_header(headers.EDIT_PRODUCTS_PAGE)
        self.edit_products.check_product_description(
            test_product.name,
            product_data.NEW_MARGARITA_DESCRIPTION
        )

    @allure.feature('UPDATE PRODUCT')
    @allure.story('Проверка редактирования поля "Цена"')
    @mark.parametrize('test_product', ['margarita'], indirect=True)
    def test_edit_price_of_product(self, test_product, auth_by_admin):
        self.edit_products.open()
        self.edit_products.click_edit_product_button(
            test_product.name
        )
        self.update_product.enter_price_of_product(
            product_data.NEW_MARGARITA_PRICE_INT
        )
        self.update_product.click_update_product_button()

        self.edit_products.check_url()
        self.edit_products.check_header(headers.EDIT_PRODUCTS_PAGE)
        self.edit_products.check_price_of_product(
            test_product.name,
            product_data.NEW_MARGARITA_PRICE_STR
        )

    @allure.feature('UPDATE PRODUCT')
    @allure.story('Проверка редактирования поля "URL картинки"')
    @mark.parametrize('test_product', ['margarita'], indirect=True)
    def test_edit_image_source_of_product(self, test_product, auth_by_admin):
        self.edit_products.open()
        self.edit_products.click_edit_product_button(
            test_product.name
        )

        self.update_product.enter_image_source(
            product_data.NEW_MARGARITA_IMAGE_URL
        )
        self.update_product.click_update_product_button()

        self.edit_products.check_url()
        self.edit_products.check_header(headers.EDIT_PRODUCTS_PAGE)
        self.edit_products.check_image_source_of_product(
            test_product.name,
            product_data.NEW_MARGARITA_IMAGE_URL
        )

    @allure.feature('NAVIGATION')
    @allure.story('Проверка перехода на страницу "Редактирование товаров"')
    @mark.parametrize('test_product', ['margarita'], indirect=True)
    def test_navigation_to_edit_products_page(self, test_product, auth_by_admin):
        self.edit_products.open()
        self.edit_products.click_edit_product_button(
            test_product.name
        )

        self.update_product.click_back_to_edit_products_page_button()

        self.edit_products.check_url()
        self.edit_products.check_header(headers.EDIT_PRODUCTS_PAGE)




