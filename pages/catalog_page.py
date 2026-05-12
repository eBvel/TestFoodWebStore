import allure

from pages.base_page import BasePage
from webstore_config.locators import CatalogLocators as locators


class CatalogPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Запрос списка "Наименования" товаров')
    def get_product_titles(self):
        return [
            product.text
            for product in self.find_elements(locators.PRODUCT_TITLES)
        ]

    def get_product_count(self, product_name):
        with allure.step(f'Запрос кол-ва товара "{product_name}" в корзине'):
            self.wait_value_change(locators.COUNT_OF_PRODUCT(product_name))
            return int(
                self
                .find_visible_element(locators.COUNT_OF_PRODUCT(product_name))
                .get_attribute('value')
            )

    def get_product_description(self, product_name):
        with allure.step(f'Запрос "Описания" товара "{product_name}"'):
            return (
                self
                .find_visible_element(
                    locators.PRODUCT_DESCRIPTION(product_name)
                )
                .text
            )

    def get_product_image_url(self, product_name):
        with allure.step(f'Запрос "URL картинки" товара "{product_name}"'):
            return self.find_visible_element(
                locators.PRODUCT_IMG(product_name)
            ).get_attribute('src')

    def get_product_price(self, product_name):
        with allure.step(f'Запрос "цены" продукта "{product_name}"'):
            return self.find_visible_element(
                locators.PRODUCT_PRICE(product_name)
            ).text

    def multiple_button_click(self, product_name, locator, click_count=1):
        for i in range(click_count):
            self.click(locator)
            self.is_attribute_present(
                locators.COUNT_OF_PRODUCT(product_name),
                'value',
                str(i+1)
            )

    def add_product(self, product_name, count=1):
        with allure.step(f"Добавление товара {product_name}"
                         f" в количестве {count} в корзину"):
            self.multiple_button_click(
                product_name,
                locators.ADD_BUTTON(product_name),
                count
            )

    def remove_product(self, product_name, count=1):
        with allure.step(f"Удаление товара {product_name}"
                         f" в количестве {count} из корзины"):
            self.multiple_button_click(
                product_name,
                locators.REMOVE_BUTTON(product_name),
                count
            )

    @allure.step('Запрос "текущего значения" счетчика корзины')
    def get_cart_counter_value(self):
        self.wait_text_change(locators.CART_COUNTER)
        return int(self.find_visible_element(locators.CART_COUNTER).text)