import allure

from pages.base_page import BasePage
from utils.assertion import AssertValues
from webstore_config.links import Links
from webstore_config.locators import CreateProductLocators as locators
from tests.test_data.test_products import Product


class CreateProductPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = Links.CREATE_PRODUCT_PAGE_URL

        self.field_locators = {
            'name': locators.NAME_FIELD,
            'description': locators.DESCRIPTION_FIELD,
            'price': locators.PRICE_FIELD,
            'image_url': locators.IMAGE_SOURCE_FIELD
        }

    def __fill_in_field(self, field_name, value, locator):
        with allure.step(f'Ввод значения "{value}" в поле "{field_name}"'):
            if value is None:
                value = ''
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

    def filling_fields(self, product: Product):
        self.enter_product_name(product.name)
        self.enter_product_description(product.description)
        self.enter_expected_category(product.category)
        self.enter_price_of_product(product.price)
        self.enter_image_source(product.image_url)

    @allure.step('Нажатие кнопки "Создать товар"')
    def click_create_product_button(self):
        self.find_clickable_element(locators.CREATE_PRODUCT_BUTTON).click()

    @allure.step('Нажатие кнопки "Обратно к товарам"')
    def click_back_to_edit_products_page_button(self):
        (
            self
            .find_clickable_element(locators.BACK_TO_EDIT_PRODUCTS_PAGE_BUTTON)
            .click()
        )

    def get_field_border_color(self, field_name):
        with allure.step(f'Запрос цвета рамки вокруг поля "{field_name}"'):
            try:
                return (
                    self
                    .find_visible_element(self.field_locators[field_name])
                    .value_of_css_property('border-color')
                )
            except KeyError as e:
                print(f'KeyError: incorrect value - {e}')
                return None

    @property
    @allure.step('Запрос состояния кнопки "Создать товар" (активна или нет)')
    def create_product_button_is_enabled(self):
        return self.find_visible_element(locators.CREATE_PRODUCT_BUTTON).is_enabled()

    def check_create_button_is_enabled(self, expected_value):
        with allure.step('Проверка, активная кнопка "Создать товар" или нет.'
                         f'Ожидаемое значение: {expected_value}'):
            AssertValues.compare_values(
                'CREATE PRODUCT: Create button is enabled',
                self.create_product_button_is_enabled,
                expected_value
            )

    def check_field_border_color(self, field_name, expected_value):
        with allure.step(f'Проверка цвета рамки вокруг поля. '
                         f'Ожидаемое значение: "{expected_value}"'):
            AssertValues.compare_values(
                f'CREATE PRODUCT: Field({field_name}) - border color',
                self.get_field_border_color(field_name),
                expected_value
            )