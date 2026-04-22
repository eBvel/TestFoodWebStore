import allure
from pages.base_page import BasePage
from utils.assertion import AssertValues
from webstore_config.locators import CatalogLocators as locators


class CatalogPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Запрос списка "Наименования" товаров.')
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

    def multiple_button_click(self, locator, click_count=1):
        button = self.find_clickable_element(locator)
        while click_count > 0:
            button.click()
            click_count -= 1


    def add_product(self, product_name, count=1):
        with allure.step(f"Добавление товара {product_name}"
                         f" в количестве {count} в корзину."):
            self.multiple_button_click(
                locators.ADD_BUTTON(product_name),
                count
            )

    def remove_product(self, product_name, count=1):
        with allure.step(f"Удаление товара {product_name}"
                         f" в количестве {count} из корзины."):
            self.multiple_button_click(
                locators.REMOVE_BUTTON(product_name),
                count
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

    def check_product_to_catalog(self, product_name):
        with allure.step(f'Проверка наличия товара "{product_name}"'
                         f' в каталоге.'):
            AssertValues.contains(
                f"CATALOG: Product name ({product_name})",
                product_name,
                self.get_product_titles()
            )

    def check_current_count_of_product(self, product_name, expected_count):
        with allure.step(f'Проверка количества товара "{product_name}" '
                         f'в корзине. Ожидаемое значение: {expected_count}'):
            check_attribute_args = (
                locators.COUNT_OF_PRODUCT(product_name),
                'value',
                str(expected_count)
            )
            current_count = self.get_product_count(product_name)
            if current_count == expected_count:
                self.is_attribute_missing(*check_attribute_args)
            else:
                self.is_attribute_present(*check_attribute_args)
            current_count = self.get_product_count(product_name)

            AssertValues.compare_values(
                f"CATALOG: Product count in cart is ({expected_count})",
                current_count,
                expected_count
            )

    def check_cart_counter_value(self, expected_value):
        with allure.step(f'Проверка текущего значения счетчика корзины.'
                         f' Ожидаемое значение: {expected_value}'):
            is_expected_count_present = self.is_text_present(
                locators.CART_COUNTER,
                str(expected_value)
            )

            AssertValues.compare_values(
                f"CATALOG: Cart counter is {expected_value}",
                is_expected_count_present,
                True
            )

    def check_product_description(self, product_name, expected_value):
        with allure.step(f'Проверка "Описания" товара "{product_name}".'
                         f' Ожидаемое значение: {expected_value}'):
            AssertValues.compare_values(
                f"CATALOG: Product description ({product_name})",
                self.get_product_description(product_name),
                expected_value
            )

    def check_product_price(self, product_name, expected_value):
        with allure.step(f'Проверка "Цены" товара "{product_name}".'
                         f' Ожидаемое значение: {expected_value}'):
            AssertValues.compare_values(
                f"CATALOG: Product price ({product_name})",
                self.get_product_price(product_name),
                expected_value
            )

    def check_product_image(self, product_name, expected_value):
        with allure.step(f'Проверка "URL картинки" товара "{product_name}".'
                         f' Ожидаемое значение: {expected_value}'):
            AssertValues.compare_values(
                f"CATALOG: Product image url ({product_name})",
                self.get_product_image_url(product_name),
                expected_value
            )