import allure

from selenium.webdriver.common.keys import Keys
from pages.create_product_page import CreateProductPage
from utils.assertion import AssertValues
from webstore_config.links import Links
from webstore_config.locators import CreateProductLocators as locators


class UpdateProductPage(CreateProductPage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = Links.UPDATE_PRODUCT_PAGE_URL

    @property
    @allure.step('Запрос идентификатора продукта')
    def product_id(self):
        return self.find_visible_element(locators.ID_FIELD).get_attribute('value')

    def enter_product_name(self, name):
        super().enter_product_name(Keys.CONTROL + 'a')
        super().enter_product_name(name)

    def enter_product_description(self, description):
        super().enter_product_description(Keys.CONTROL + 'a')
        super().enter_product_description(description)

    def enter_price_of_product(self, price):
        super().enter_price_of_product(Keys.CONTROL + 'a')
        super().enter_price_of_product(price)

    def enter_image_source(self, url):
        super().enter_image_source(Keys.CONTROL + 'a')
        super().enter_image_source(url)

    @allure.step('Нажатие кнопки "Обновить товар"')
    def click_update_product_button(self):
        self.click_create_product_button()

    def check_url(self):
        id = self.product_id
        AssertValues.compare_values(
            "UPDATE PRODUCT: URL OF PAGE",
            self.get_current_url(),
            self.url+id
        )