import allure
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
        return self.find_visible_element(locators.ID_FIELD).text

    def click_update_product_button(self):
        self.click_create_product_button()

    def check_url(self):
        AssertValues.compare_values(
            "",
            self.url + self.product_id,
            self.get_current_url()
        )