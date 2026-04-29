import allure

from pytest import mark
from pages.catalog_page import CatalogPage
from tests.test_data.pages_data import CatalogData
from tests.test_data.datasets import Datasets
from tests.test_data.expected_values import ExpectedValues as EV


class TestCatalogPage:
    @classmethod
    def setup_class(cls):
        cls.catalog = CatalogPage(cls.driver)

    @allure.feature('PRODUCT DATA')
    @allure.story('Поиск товара по "Имени" в каталоге')
    @mark.parametrize('test_product', ['sandwich'], indirect=True)
    def test_search_product(self, test_product, auth_by_user1):
        self.catalog.open()

        self.catalog.check_product_to_catalog(test_product.name)

    @allure.feature('PRODUCT DATA')
    @allure.story('Проверка поля "Описание" у карточки товара')
    @mark.parametrize('test_product', ['sandwich'], indirect=True)
    def test_presence_description_of_product(
            self,
            test_product,
            auth_by_user1
    ):
        self.catalog.open()

        self.catalog.check_product_description(
            test_product.name,
            test_product.description
        )

    @allure.feature('PRODUCT DATA')
    @allure.story('Проверка поля "Цена" у карточки товара')
    @mark.parametrize('test_product', ['sandwich'], indirect=True)
    def test_presence_price_of_product(self, test_product, auth_by_user1):
        self.catalog.open()

        self.catalog.check_product_price(
            test_product.name,
            test_product.get_price_str()
        )

    @allure.feature('PRODUCT DATA')
    @allure.story('Проверка поля "URL картинки" у карточки товара')
    @mark.parametrize('test_product', ['sandwich'], indirect=True)
    def test_presence_image_of_product(self, test_product, auth_by_user1):
        self.catalog.open()

        self.catalog.check_product_image(
            test_product.name,
            test_product.image_url
        )

    @allure.feature('ADD/REMOVE PRODUCT TO CART')
    @allure.story('Проверка добавления товара в корзину по кнопке "+"')
    @mark.parametrize('test_product', ['sandwich'], indirect=True)
    def test_add_product_to_cart(self, test_product, auth_by_user1):
        self.catalog.open()
        self.catalog.add_product(test_product.name)

        self.catalog.check_current_count_of_product(
            test_product.name,
            EV.CATALOG_COUNT_AFTER_ADD
        )

    @allure.feature('ADD/REMOVE PRODUCT TO CART')
    @allure.story('Проверка удаления товара из корзины по кнопке "-"')
    @mark.parametrize('test_product', ['sandwich'], indirect=True)
    def test_remove_product_from_cart(self, test_product, auth_by_user1):
        self.catalog.open()
        self.catalog.add_product(test_product.name)
        self.catalog.remove_product(test_product.name)

        self.catalog.check_current_count_of_product(
            test_product.name,
           EV.CATALOG_COUNT_AFTER_REMOVE
        )

    @allure.feature('PRODUCT COUNTER')
    @allure.story('Проверка "шага" изменения кол-ва товаров в корзине')
    @mark.parametrize('test_product', ['sandwich'], indirect=True)
    @mark.parametrize(
        "add_count, remove_count",
        Datasets.CATALOG_STEP_OF_COUNT
    )
    def test_step_of_count_changes(
            self,
            test_product,
            auth_by_user1,
            add_count,
            remove_count
    ):
        self.catalog.open()
        self.catalog.add_product(test_product.name, add_count)

        self.catalog.check_current_count_of_product(
            test_product.name,
            add_count
        )

        self.catalog.remove_product(test_product.name, remove_count)

        self.catalog.check_current_count_of_product(
            test_product.name,
            add_count - remove_count
        )

    @allure.feature('CART COUNTER')
    @allure.story('Проверка счетчика товаров в корзине')
    @mark.parametrize('test_product', ['sandwich'], indirect=True)
    @mark.parametrize('quantity', Datasets.CATALOG_CART_COUNTER)
    def test_cart_counter_changes(
            self,
            test_product,
            quantity,
            auth_by_user1
    ):
        self.catalog.open()
        self.catalog.add_product(test_product.name, quantity)

        self.catalog.check_cart_counter_value(quantity)

    @allure.feature('PRODUCT COUNTER')
    @allure.story('Проверка нижней границы (0) счетчика товаров')
    @mark.parametrize('test_product', ['sandwich'], indirect=True)
    def test_lower_limit_of_counter(self, test_product, auth_by_user1):
        self.catalog.open()
        self.catalog.remove_product(test_product.name)

        self.catalog.check_current_count_of_product(
            test_product.name,
            CatalogData.MIN_PRODUCT_COUNT
        )

    @allure.feature('PRODUCT COUNTER')
    @allure.story('Проверка верхней границы (100) счетчика товаров')
    @mark.parametrize('test_product', ['sandwich'], indirect=True)
    @mark.parametrize(
        'start_product_count',
        Datasets.CATALOG_UPPER_LIMIT_OF_PRODUCT_COUNTER
    )
    def test_max_limit_of_counter(
            self,
            test_product,
            start_product_count,
            auth_by_user1,
            product_count_to_cart
    ):
        self.catalog.open()
        product_count_to_cart(test_product, start_product_count)
        self.catalog.add_product(test_product.name)

        self.catalog.check_current_count_of_product(
            test_product.name,
            CatalogData.MAX_PRODUCT_COUNT
        )