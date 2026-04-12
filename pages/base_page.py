import allure
from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

from utils.assertion import AssertValues
from webstore_config.links import Links
from webstore_config.locators import BaseLocators as locators


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = Links.BASE_URL

    def open(self):
        with allure.step(f"Открытие страницы по ссылке: {self.url}"):
            self.driver.maximize_window()
            self.driver.get(self.url)

    def find(self, condition, timeout):
        with allure.step(f'Поиск элемента страницы "{self.url}". '
                         f'Локатор: "{condition}"'):
            return wait(self.driver, timeout).until(condition)

    def find_visible_element(self, locator, timeout=10):
        return self.find(EC.visibility_of_element_located(locator), timeout)

    def find_clickable_element(self, locator, timeout=10):
        element = self.find(EC.element_to_be_clickable(locator), timeout)
        self.scroll_to_element(element)
        return element

    def find_presence_element(self, locator, timeout=10):
        return self.find(EC.presence_of_element_located(locator), timeout)

    def find_elements(self, locator, timeout=10):
        return self.find(
            EC.visibility_of_all_elements_located(locator),
            timeout
        )

    def scroll_to_element(self, element):
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center', inline:'center'})",
            element
        )

    @property
    def header(self):
        with allure.step(f'Запрос заголовка страницы: '
                         f'"{self.__class__.__name__}"'):
            try:
                return self.find_visible_element(locators.HEADER, 3).text
            except Exception:
                return None

    @allure.step("Нажатие кнопки навигации (меню).")
    def click_navigation_bar(self):
        self.find_clickable_element(locators.NAVIGATION_BAR).click()

    @allure.step("Нажатие на заголовок 'Магазин'.")
    def click_header_button(self):
        self.find_clickable_element(locators.HEADER_BUTTON).click()

    @allure.step("Нажатие кнопки 'Корзинка'.")
    def click_cart_button(self):
        self.find_clickable_element(locators.CART_BUTTON).click()

    @allure.step("Запрос текста заголовка.")
    def get_header_text(self):
        return self.find_visible_element(locators.HEADER_BUTTON, 3).text

    @allure.step("Запрос текущего URL страницы.")
    def get_current_url(self):
        return self.driver.current_url

    def check_header(self, expected_title):
        with allure.step(f'Проверка заголовка страницы '
                         f'"{self.__class__.__name__}". Ожидаемое значение: '
                         f'"{expected_title}"'):
            AssertValues.compare_values(
                f"{self.__class__.__name__} HEADER",
                self.header,
                expected_title
            )

    def check_url(self):
        with allure.step(f'Проверка URL текущей страницы '
                         f'"{self.__class__.__name__}". Ожидаемое значение: '
                         f'"{self.url}"'):
            AssertValues.compare_values(
                f"{self.__class__.__name__} URL",
                self.get_current_url(),
                self.url
            )