import time

import allure
from pages.base_page import BasePage
from utils.assertion import AssertValues
from webstore_config.locators import CatalogLocators as locators


class CatalogPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @property
    @allure.step('Запрос текста заголовка страницы "Каталог".')
    def header(self):
        return self.find_visible_element(locators.HEADER, 5).text

    @allure.step('Запрос списка "Наивенования" товаров.')
    def get_product_titles(self):
        return [
            product.text
            for product in self.find_elements(locators.PRODUCT_TITLES)
        ]

    def get_product_count(self, product_name):
        with allure.step(f'Запрос кол-ва товара "{product_name}" в корзине.'):
            return int(self.find_visible_element(
                locators.COUNT_OF_PRODUCT(product_name)
            ).get_attribute('value'))

    def check_product_to_catalog(self, product_name):
        with allure.step(f'Проверка наличия товара "{product_name}"'
                         f' в каталоге.'):
            products = self.get_product_titles()
            AssertValues.contains(
                f"CATALOG: PRODUCT({product_name}) NAME",
                product_name,
                products
            )

    def get_product_description(self, product_name):
        with allure.step(f'Запрос "Описания" товара "{product_name}".'):
            return self.find_visible_element(
                locators.PRODUCT_DESCRIPTION(product_name)
            ).text

    def get_product_image_url(self, product_name):
        with allure.step(f'Запрос "URL картинки" товара "{product_name}".'):
            return self.find_visible_element(
                locators.PRODUCT_IMG(product_name)
            ).get_attribute('src')

    def get_product_price(self, product_name):
        with allure.step(f'Запрос "цены" продукта "{product_name}"'):
            return self.find_visible_element(
                locators.PRODUCT_PRICE(product_name)
            ).text

    def add_product(self, product_name, count=1):
        with allure.step(f"Добавление товара {product_name}"
                         f" в количестве {count} в корзину."):
            add_button = self.find_clickable_element(
                locators.ADD_BUTTON(product_name)
            )
            while count > 0:
                add_button.click()
                count -= 1
                time.sleep(0.2)

    def remove_product(self, product_name, count=1):
        with allure.step(f"Удаление товара {product_name}"
                         f" в количестве {count} из корзины."):
            remove_button = self.find_clickable_element(
                locators.REMOVE_BUTTON(product_name)
            )
            while count > 0:
                remove_button.click()
                count -= 1
                time.sleep(0.2)

    def check_current_count_of_product(self, product_name, expected_count):
        with allure.step(f'Проверка количества товара "{product_name}" '
                         f'в корзине. Ожидаемое значение: {expected_count}'):
            current_count = self.get_product_count(product_name)
            AssertValues.compare_values(
                f"CATALOG: PRODUCT({product_name}) COUNT IN CART",
                current_count,
                expected_count
            )

    def clear_product_counter(self, product_name):
        with allure.step(f'Запрос на обнуление счетчика товара '
                         f'"{product_name}" в корзине.'):
            count = self.get_product_count(product_name)
            if count > 0:
                self.remove_product(product_name, count)

    @allure.step('Запрос на удаление всех товаров из корзины:')
    def clear_all_products_counter(self):
        products = self.get_product_titles()
        for product in products:
            self.clear_product_counter(product)

    @allure.step('Запрос "текущего значения" счетчика корзины.')
    def get_cart_counter_value(self):
        return int(self.find_visible_element(locators.CART_COUNTER).text)

    def check_cart_counter_value(self, expected_value):
        with allure.step(f'Проверка текущего значения счетчика корзины.'
                         f' Ожидаемое значение: {expected_value}'):
            current_value = self.get_cart_counter_value()
            AssertValues.compare_values(
                "CATALOG: CART COUNTER",
                current_value,
                expected_value
            )

    def check_max_limit(self, product_name, limit):
        with allure.step(f'Проверка текущего количества товара '
                         f'"{product_name}" на превышение лимита в '
                         f'"{limit}" единиц.'):
            AssertValues.is_smaller_or_equal(
                f"CATALOG: MAX LIMIT OF PRODUCT({product_name}) COUNT",
                self.get_product_count(product_name),
                limit
            )

    def check_product_description(self, product_name, expected_value):
        with allure.step(f'Проверка "Описания" товара "{product_name}".'
                         f' Ожидаемое значение: {expected_value}'):
            AssertValues.compare_values(
                f"CATALOG: PRODUCT({product_name}) DESCRIPTION",
                self.get_product_description(product_name),
                expected_value
            )

    def check_product_price(self, product_name, expected_value):
        with allure.step(f'Проверка "Цены" товара "{product_name}".'
                         f' Ожидаемое значение: {expected_value}'):
            AssertValues.compare_values(
                f"CATALOG: PRODUCT({product_name}) PRICE",
                self.get_product_price(product_name),
                expected_value
            )

    def check_product_image(self, product_name, expected_value):
        with allure.step(f'Проверка "URL картинки" товара "{product_name}".'
                         f' Ожидаемое значение: {expected_value}'):
            AssertValues.compare_values(
                f"CATALOG: PRODUCT({product_name}) IMAGE URL",
                self.get_product_image_url(product_name),
                expected_value
            )