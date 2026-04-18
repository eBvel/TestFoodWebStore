import allure
import pytest

from pages.catalog_page import CatalogPage
from tests.test_data import product_data


class TestCatalogPage:
    @classmethod
    def setup_class(cls):
        cls.catalog = CatalogPage(cls.driver)

    @allure.feature('PRODUCT DATA')
    @allure.story('Поиск товара по "Имени" в каталоге')
    @pytest.mark.parametrize('product', ['sandwich'], indirect=True)
    def test_search_product(self, product, auth_by_user1):
        self.catalog.open()
        self.catalog.check_product_to_catalog(product.name)

    @allure.feature('PRODUCT DATA')
    @allure.story('Проверка поля "Описание" у карточки товара')
    @pytest.mark.parametrize('product', ['sandwich'], indirect=True)
    def test_presence_description_of_product(self, product, auth_by_user1):
        self.catalog.open()
        self.catalog.check_product_description(
            product.name,
            product.description
        )

    @allure.feature('PRODUCT DATA')
    @allure.story('Проверка поля "Цена" у карточки товара')
    @pytest.mark.parametrize('product', ['sandwich'], indirect=True)
    def test_presence_price_of_product(self, product, auth_by_user1):
        self.catalog.open()
        self.catalog.check_product_price(
            product.name,
            product.get_price_str()
        )

    @allure.feature('PRODUCT DATA')
    @allure.story('Проверка поля "URL картинки" у карточки товара')
    @pytest.mark.parametrize('product', ['sandwich'], indirect=True)
    def test_presence_image_of_product(self, product, auth_by_user1):
        self.catalog.open()
        self.catalog.check_product_image(
            product.name,
            product.image_url
        )

    @allure.feature('ADD/REMOVE PRODUCT TO CART')
    @allure.story('Проверка добавления товара в корзину по кнопке "+"')
    @pytest.mark.parametrize('product', ['sandwich'], indirect=True)
    def test_add_product_to_cart(self, product, auth_by_user1):
        self.catalog.open()
        self.catalog.add_product(product.name)
        self.catalog.check_current_count_of_product(
            product.name,
            1
        )

    @allure.feature('ADD/REMOVE PRODUCT TO CART')
    @allure.story('Проверка удаления товара из корзины по кнопке "-"')
    @pytest.mark.parametrize('product', ['sandwich'], indirect=True)
    def test_remove_product_from_cart(self, product, auth_by_user1):
        self.catalog.open()
        self.catalog.add_product(product.name)
        self.catalog.remove_product(product.name)
        self.catalog.check_current_count_of_product(
            product.name,
           0
        )

    @allure.feature('PRODUCT COUNTER')
    @allure.story('Проверка "шага" изменения кол-ва товаров в корзине')
    @pytest.mark.parametrize('product', ['sandwich'], indirect=True)
    @pytest.mark.parametrize("add_count, remove_count", [(2, 1), (5, 3)])
    def test_step_of_count_changes(
            self,
            product,
            auth_by_user1,
            add_count,
            remove_count
    ):
        self.catalog.open()
        self.catalog.add_product(product.name, add_count)
        self.catalog.check_current_count_of_product(
            product.name,
            add_count
        )

        self.catalog.remove_product(product.name, remove_count)
        self.catalog.check_current_count_of_product(
            product.name,
            add_count - remove_count
        )

    @allure.feature('CART COUNTER')
    @allure.story('Проверка счетчика товаров в корзине')
    @pytest.mark.parametrize('product', ['sandwich'], indirect=True)
    def test_cart_counter_changes(self, product, auth_by_user1):
        self.catalog.open()
        self.catalog.add_product(product.name, 1)
        self.catalog.check_cart_counter_value(1)

    @allure.feature('PRODUCT COUNTER')
    @allure.story('Проверка нижней границы (0) счетчика товаров')
    @pytest.mark.parametrize('product', ['sandwich'], indirect=True)
    def test_lower_limit_of_counter(self, product, auth_by_user1):
        self.catalog.open()
        self.catalog.remove_product(product.name)
        self.catalog.check_current_count_of_product(
            product.name,
            product_data.MIN_LIMIT
        )

    @allure.feature('PRODUCT COUNTER')
    @allure.story('Проверка верхней границы (100) счетчика товаров')
    @pytest.mark.parametrize('product', ['sandwich'], indirect=True)
    def test_max_limit_of_counter(self, product, auth_by_user1, product_count_to_cart):
        self.catalog.open()
        product_count_to_cart(product, 100)
        self.catalog.refresh()
        self.catalog.check_current_count_of_product(
            product.name,
            product_data.MAX_LIMIT
        )

        self.catalog.add_product(product.name)
        self.catalog.check_current_count_of_product(
            product_data.SANDWICH_NAME,
            product_data.MAX_LIMIT
        )