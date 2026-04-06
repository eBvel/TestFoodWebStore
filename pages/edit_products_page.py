import allure
from pages.base_page import BasePage
from utils.assertion import AssertValues
from webstore_config.links import Links
from webstore_config.locators import EditProductsLocators as locators


class EditProductsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = Links.EDIT_PRODUCTS_PAGE_URL

    @property
    @allure.step('Запрос заголовка страницы "Редактирование товаров"')
    def header(self):
        return self.find_visible_element(locators.HEADER).text

    @allure.step('Нажатие кнопки "Добавить товар"')
    def click_create_product_button(self):
        self.find_clickable_element(locators.CREATE_PRODUCT_BUTTON).click()

    def click_edit_product_button(self, product_name):
        with allure.step(f'ТОВАР "{product_name}": нажатие кнопки "Редактировать"'):
            self.find_clickable_element(locators.EDIT_PRODUCT_BUTTON(product_name)).click()

    def click_delete_product_button(self, product_name):
        with allure.step(f'ТОВАР "{product_name}": нажатие кнопки "Удалить"'):
            self.find_clickable_element(locators.DELETE_PRODUCT_BUTTON(product_name)).click()

    def product_is_exists(self, product_name):
        with allure.step(f'Проверка, существует ли товар '
                         f'"{product_name}" в каталоге'):
            try:
                self.find_elements(locators.PRODUCT_IS_EXISTS(product_name))
                return True
            except Exception:
                return False

    def check_product_is_exists(self, product_name, expected_value):
        with allure.step(f'Проверка наличия товара "{product_name}" в '
                         f'каталоге. Ожидаемое значение: {expected_value}'):
            AssertValues.compare_values(
                "EDIT PRODUCTS: PRODUCT IS EXISTS",
                self.product_is_exists(product_name),
                expected_value
            )