import allure
from webstore_config.locators import NavigationBarLocators as locators
from pages.base_page import BasePage


class NavigationBarPage(BasePage):
    @property
    def header(self):
        return self.find_visible_element(locators.HEADER).text

    @allure.step('Нажатие кнопки "Редактировать товары" в окне навигации.')
    def click_edit_products_button(self):
        self.find_clickable_element(locators.EDIT_PRODUCTS_BUTTON).click()

    @allure.step('Нажатие кнопки "Каталог" в окне навигации.')
    def click_catalog_button(self):
        self.find_clickable_element(locators.CATALOG_BUTTON).click()

    @allure.step('Нажатие кнопки "Корзинка" в окне навигации.')
    def click_cart_button(self):
        self.find_clickable_element(locators.CART_BUTTON).click()

    @allure.step('Нажатие кнопки "Выход" в окне навигации.')
    def click_log_out(self):
        self.find_clickable_element(locators.LOGOUT_BUTTON).click()