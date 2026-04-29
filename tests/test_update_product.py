import allure

from pytest import mark
from pages.create_product_page import CreateProductPage
from pages.update_product_page import UpdateProductPage
from pages.edit_products_page import EditProductsPage
from tests.test_data.pages_data import UpdateProductData, EditProductsData
from tests.test_data.new_product_data import NewProductData
from tests.test_data.expected_values import ExpectedValues as EV


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
        self.update_product.check_header(UpdateProductData.HEADER)

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
        self.update_product.enter_product_name(NewProductData.NAME)
        self.update_product.click_update_product_button()
        self.edit_products.check_url()
        self.edit_products.check_header(EditProductsData.HEADER)

        self.edit_products.check_existence_of_product(
            NewProductData.NAME,
            EV.UPDATE_PRODUCT_IS_EXIST
        )

    @allure.feature('UPDATE PRODUCT')
    @allure.story('Проверка редактирования поля "Описание"')
    @mark.parametrize('test_product', ['margarita'], indirect=True)
    def test_edit_description_of_product(self, test_product, auth_by_admin):
        self.edit_products.open()
        self.edit_products.click_edit_product_button(test_product.name)
        self.update_product.enter_product_description(
            NewProductData.DESCRIPTION
        )
        self.update_product.click_update_product_button()

        self.edit_products.check_url()
        self.edit_products.check_header(EditProductsData.HEADER)
        self.edit_products.check_product_description(
            test_product.name,
            NewProductData.DESCRIPTION
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
            NewProductData.PRICE_INT
        )
        self.update_product.click_update_product_button()

        self.edit_products.check_url()
        self.edit_products.check_header(EditProductsData.HEADER)
        self.edit_products.check_price_of_product(
            test_product.name,
            NewProductData.PRICE_STR
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
            NewProductData.IMAGE_URL
        )
        self.update_product.click_update_product_button()

        self.edit_products.check_url()
        self.edit_products.check_header(EditProductsData.HEADER)
        self.edit_products.check_image_source_of_product(
            test_product.name,
            NewProductData.IMAGE_URL
        )

    @allure.feature('NAVIGATION')
    @allure.story('Проверка перехода на страницу "Редактирование товаров"')
    @mark.parametrize('test_product', ['margarita'], indirect=True)
    def test_navigation_to_edit_products_page(
            self,
            test_product,
            auth_by_admin
    ):
        self.edit_products.open()
        self.edit_products.click_edit_product_button(
            test_product.name
        )
        self.update_product.click_back_to_edit_products_page_button()

        self.edit_products.check_url()
        self.edit_products.check_header(EditProductsData.HEADER)