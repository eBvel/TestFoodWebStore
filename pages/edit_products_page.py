import allure

from selenium.common import TimeoutException
from pages.base_page import BasePage
from webstore_config.links import Links
from webstore_config.locators import EditProductsLocators as locators


class EditProductsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = Links.EDIT_PRODUCTS_PAGE_URL

    def get_product_description(self, product_name):
        with allure.step(f'Запрос значения поля "Описания" '
                         f'у карточки товара "{product_name}"'):
            return (
                self
                .find_visible_element(
                    locators.PRODUCT_DESCRIPTION(product_name)
                )
                .text
            )

    def get_product_price(self, product_name):
        with allure.step(f'Запрос значения поля "Цена" '
                         f'у карточки товара "{product_name}"'):
            return (
                self
                .find_visible_element(locators.PRODUCT_PRICE(product_name))
                .text
                .split(': ')[1]
            )

    def get_product_image_url(self, product_name):
        with allure.step(f'Запрос значения поля "URL картинки" '
                         f'у карточки товара "{product_name}"'):
            return (
                self
                .find_visible_element(
                    locators.PRODUCT_IMAGE_URL(product_name)
                )
                .get_attribute('src')
            )

    @allure.step('Нажатие кнопки "Добавить товар"')
    def click_create_product_button(self):
        self.click(locators.CREATE_PRODUCT_BUTTON)

    def click_edit_product_button(self, product_name):
        with allure.step(f'ТОВАР "{product_name}": '
                         f'нажатие кнопки "Редактировать"'):
            self.click(locators.EDIT_PRODUCT_BUTTON(product_name))

    def click_delete_product_button(self, product_name):
        with allure.step(f'ТОВАР "{product_name}": нажатие кнопки "Удалить"'):
            self.click(locators.DELETE_PRODUCT_BUTTON(product_name))


    def product_is_missing(self, product_name):
        with allure.step(f'Проверка, существует ли товар '
                         f'"{product_name}" в каталоге'):
            try:
                return self.is_invisible(
                    locators.PRODUCT_IS_EXISTS(product_name)
                )
            except TimeoutException:
                return False

    def is_product_exists(self, product_name):
        return not self.product_is_missing(product_name)
