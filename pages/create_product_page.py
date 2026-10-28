import allure

from pages.base_page import BasePage, WebDriver
from webstore_config.links import Links
from webstore_config.locators import (CreateProductLocators as locators,
                                      LocatorType)
from tests.test_data.test_products import Product


class CreateProductPage(BasePage):
    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
        self.url = Links.CREATE_PRODUCT_PAGE_URL

        self.field_locators = {
            'name': locators.NAME_FIELD,
            'description': locators.DESCRIPTION_FIELD,
            'price': locators.PRICE_FIELD,
            'image_url': locators.IMAGE_SOURCE_FIELD
        }

    def __fill_in_field(
            self,
            field_name: str,
            value: str | float,
            locator: LocatorType
    ) -> None:
        with allure.step(f'Ввод значения "{value}" в поле "{field_name}"'):
            (
                self
                .find_visible_element(locator)
                .send_keys(value if value is not None else '')
            )

    def enter_product_name(self, name: str) -> None:
        self.__fill_in_field("Наименование", name, locators.NAME_FIELD)

    def enter_product_description(self, description: str) -> None:
        self.__fill_in_field(
            "Описание",
            description,
            locators.DESCRIPTION_FIELD
        )

    def enter_expected_category(self, expected_category: str) -> None:
        self.__fill_in_field(
            "Ожидаемая категория",
            expected_category,
            locators.EXPECTED_CATEGORY_FIELD
        )

    def enter_price_of_product(self, price: float) -> None:
        self.__fill_in_field("Цена", price, locators.PRICE_FIELD)

    def enter_image_source(self, url: str) -> None:
        self.__fill_in_field("URL картинки", url, locators.IMAGE_SOURCE_FIELD)

    def filling_fields(self, product: Product) -> None:
        self.enter_product_name(product.name)
        self.enter_product_description(product.description)
        self.enter_expected_category(product.category)
        self.enter_price_of_product(product.price)
        self.enter_image_source(product.image_url)

    @allure.step('Нажатие кнопки "Создать товар"')
    def click_create_product_button(self) -> None:
        self.click(locators.CREATE_PRODUCT_BUTTON)

    @allure.step('Нажатие кнопки "Обратно к товарам"')
    def click_back_to_edit_products_page_button(self) -> None:
        self.click(locators.BACK_TO_EDIT_PRODUCTS_PAGE_BUTTON)

    def get_field_border_color(self, field_name: str) -> str | None:
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

    @allure.step('Запрос состояния кнопки "Создать товар" (активна или нет)')
    def is_create_button_enabled(self) -> bool:
        return (
            self
            .find_visible_element(locators.CREATE_PRODUCT_BUTTON)
            .is_enabled()
        )