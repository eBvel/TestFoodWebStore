import allure

from pytest import mark
from pages.create_product_page import CreateProductPage
from pages.update_product_page import UpdateProductPage
from pages.edit_products_page import EditProductsPage
from tests.test_data.pages_data import EditProductsData
from tests.test_data.new_product_data import NewProductData
from tests.test_data.expected_values import ExpectedValues as EV
from utils.assertion import Assert


class TestUpdateProductPage:
    @classmethod
    def setup_class(cls):
        cls.edit_products = EditProductsPage(cls.driver)
        cls.create_product = CreateProductPage(cls.driver)
        cls.update_product = UpdateProductPage(cls.driver)

    @allure.feature('FUNCTIONAL')
    @allure.story('Проверка редактирования поля "Наименование"')
    @mark.smoke
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

        Assert.check_url(self.edit_products)
        Assert.check_header(self.edit_products, EditProductsData.HEADER)
        Assert.compare_values(
            value_name='Product is exists (changed name)',
            current_value=self.edit_products.is_product_exists(
                NewProductData.NAME
            ),
            expected_value=EV.UPDATE_PRODUCT_IS_EXIST
        )

    @allure.feature('FUNCTIONAL')
    @allure.story('Проверка редактирования поля "Описание"')
    @mark.smoke
    @mark.parametrize('test_product', ['margarita'], indirect=True)
    def test_edit_description_of_product(self, test_product, auth_by_admin):
        self.edit_products.open()
        self.edit_products.click_edit_product_button(test_product.name)
        self.update_product.enter_product_description(
            NewProductData.DESCRIPTION
        )
        self.update_product.click_update_product_button()

        Assert.check_url(self.edit_products)
        Assert.check_header(self.edit_products, EditProductsData.HEADER)
        Assert.compare_values(
            value_name='Product description (changed)',
            current_value=self.edit_products.get_product_description(
                test_product.name
            ),
            expected_value=NewProductData.DESCRIPTION
        )

    @allure.feature('FUNCTIONAL')
    @allure.story('Проверка редактирования поля "Цена"')
    @mark.smoke
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

        Assert.check_url(self.edit_products)
        Assert.check_header(self.edit_products, EditProductsData.HEADER)
        Assert.compare_values(
            value_name='Product price (changed)',
            current_value=self.edit_products.get_product_price(
                test_product.name
            ),
            expected_value=NewProductData.PRICE_STR
        )

    @allure.feature('FUNCTIONAL')
    @allure.story('Проверка редактирования поля "URL картинки"')
    @mark.smoke
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

        Assert.check_url(self.edit_products)
        Assert.check_header(self.edit_products, EditProductsData.HEADER)
        Assert.compare_values(
            value_name='Product image source (changed)',
            current_value=self.edit_products.get_product_image_url(
                test_product.name
            ),
            expected_value=NewProductData.IMAGE_URL
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

        Assert.check_url(self.edit_products)
        Assert.check_header(self.edit_products, EditProductsData.HEADER)