import allure

from pages.base_page import BasePage
from webstore_config.links import Links
from webstore_config.locators import CreateProductLocators as locators


class CreateProductPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = Links.CREATE_PRODUCT_PAGE_URL

    @property
    @allure.step('Запрос заголовка страницы создания нового товара')
    def header(self):
        return self.find_visible_element(locators.HEADER).text

    def __fill_in_field(self, field_name, value, locator):
        with allure.step(f'Ввод значения "{value}" в поле "{field_name}"'):
            self.find_visible_element(locator).send_keys(value)

    def enter_product_name(self, name):
        self.__fill_in_field("Наименование", name, locators.NAME_FIELD)

    def enter_product_description(self, description):
        self.__fill_in_field(
            "Описание",
            description,
            locators.DESCRIPTION_FIELD
        )

    def enter_expected_category(self, expected_category):
        self.__fill_in_field(
            "Ожидаемая категория",
            expected_category,
            locators.EXPECTED_CATEGORY_FIELD
        )

    def enter_category_in_list(self, category):
        self.__fill_in_field(
            "Категория в списке",
            category,
            locators.CATEGORY_IN_LIST_FIELD
        )

    def enter_price_of_product(self, price):
        self.__fill_in_field("Цена", price, locators.PRICE_FIELD)

    def enter_image_source(self, url):
        self.__fill_in_field("URL картинки", url, locators.IMAGE_SOURCE_FIELD)

    def click_create_product_button(self):
        self.find_clickable_element(locators.CREATE_PRODUCT_BUTTON).click()


