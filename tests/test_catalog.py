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
    def test_search_product(self, auth_by_user1):
        self.catalog.open()
        self.catalog.check_product_to_catalog(product_data.NAME)

    @allure.feature('PRODUCT DATA')
    @allure.story('Проверка поля "Описание" у карточки товара')
    def test_presence_description_of_product(self, auth_by_user1):
        self.catalog.open()
        self.catalog.check_product_description(
            product_data.NAME,
            product_data.DESCRIPTION
        )

    @allure.feature('PRODUCT DATA')
    @allure.story('Проверка поля "Цена" у карточки товара')
    def test_presence_price_of_product(self, auth_by_user1):
        self.catalog.open()
        self.catalog.check_product_price(
            product_data.NAME,
            product_data.PRICE
        )

    @allure.feature('PRODUCT DATA')
    @allure.story('Проверка поля "URL картинки" у карточки товара')
    def test_presence_image_of_product(self, auth_by_user1):
        self.catalog.open()
        self.catalog.check_product_image(
            product_data.NAME,
            product_data.IMAGE_URL
        )

    @allure.feature('ADD/REMOVE PRODUCT TO CART')
    @allure.story('Проверка добавления товара в корзину по кнопке "+"')
    def test_add_product_to_cart(self, auth_by_user1):
        self.catalog.open()
        before_add_count = self.catalog.get_product_count(product_data.NAME)

        if before_add_count >= product_data.MAX_LIMIT:
            remove_count = before_add_count - product_data.MAX_LIMIT + 1
            self.catalog.remove_product(
                product_data.NAME,
                remove_count
            )
            before_add_count -= remove_count

        self.catalog.add_product(product_data.NAME)
        self.catalog.check_current_count_of_product(
            product_data.NAME,
            before_add_count+1
        )

    @allure.feature('ADD/REMOVE PRODUCT TO CART')
    @allure.story('Проверка удаления товара из корзины по кнопке "-"')
    def test_remove_product_from_cart(self, auth_by_user1):
        self.catalog.open()
        self.catalog.add_product(product_data.NAME)
        before_remove_count = self.catalog.get_product_count(
            product_data.NAME
        )

        self.catalog.remove_product(product_data.NAME)
        self.catalog.check_current_count_of_product(
            product_data.NAME,
            before_remove_count - 1
        )

    @allure.feature('PRODUCT COUNTER')
    @allure.story('Проверка "шага" изменения кол-ва товаров в корзине')
    @pytest.mark.parametrize("add_count, remove_count", [(2, 1), (5, 3)])
    def test_step_of_count_changes(
            self,
            auth_by_user1,
            add_count,
            remove_count
    ):
        self.catalog.open()
        current_count = self.catalog.get_product_count(product_data.NAME)

        if current_count > product_data.MAX_LIMIT - add_count:
            self.catalog.remove_product(product_data.NAME, add_count)
            current_count -= add_count

        self.catalog.add_product(product_data.NAME, add_count)
        self.catalog.check_current_count_of_product(
            product_data.NAME,
            current_count + add_count
        )

        self.catalog.remove_product(product_data.NAME, remove_count)
        self.catalog.check_current_count_of_product(
            product_data.NAME,
            current_count + add_count - remove_count
        )

    @allure.feature('CART COUNTER')
    @allure.story('Проверка счетчика товаров в корзине')
    def test_cart_counter_changes(self, auth_by_user1):
        self.catalog.open()
        current_cart_counter_value = self.catalog.get_cart_counter_value()

        if current_cart_counter_value >= product_data.MAX_LIMIT:
            remove_count = (current_cart_counter_value
                            - product_data.MAX_LIMIT
                            + 1)
            self.catalog.remove_product(
                product_data.NAME,
                remove_count
            )
            current_cart_counter_value -= remove_count

        self.catalog.add_product(product_data.NAME)
        self.catalog.check_cart_counter_value(current_cart_counter_value + 1)

    @allure.feature('PRODUCT COUNTER')
    @allure.story('Проверка нижней границы (0) счетчика товаров')
    def test_lower_limit_of_counter(self, auth_by_user1):
        self.catalog.open()
        self.catalog.clear_product_counter(product_data.NAME)

        self.catalog.remove_product(product_data.NAME)
        self.catalog.check_current_count_of_product(
            product_data.NAME,
            product_data.MIN_LIMIT
        )

    @allure.feature('PRODUCT COUNTER')
    @allure.story('Проверка верхней границы (100) счетчика товаров')
    def test_max_limit_of_counter(self, auth_by_user1):
        self.catalog.open()
        # Проверяем, что текущее кол-во товара меньше или равно "100".
        # Если значение выше, то получим исключение.
        self.catalog.check_max_limit(product_data.NAME, product_data.MAX_LIMIT)

        current_count = self.catalog.get_product_count(product_data.NAME)
        change_count = product_data.MAX_LIMIT - current_count

        # Увеличиваем кол-во товара до 100 ед. И проверяем, что кол-во
        # равно 100 единицам.
        self.catalog.add_product(product_data.NAME, change_count)
        self.catalog.check_current_count_of_product(product_data.NAME, product_data.MAX_LIMIT)

        # Текущее кол-во = 100 ед. Добавляем 1 ед. товара. Проверяем,
        # что кол-во не изменилось и осталось равно 100 ед. (максимум
        # для одного товара).
        self.catalog.add_product(product_data.NAME)
        self.catalog.check_current_count_of_product(product_data.NAME, product_data.MAX_LIMIT)