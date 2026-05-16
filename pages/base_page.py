import allure

from collections.abc import Callable
from typing import TypeVar, Literal
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import TimeoutException
from selenium.common import ElementClickInterceptedException
from utils.conditions import WaitValueChanges, WaitTextChanges
from webstore_config.links import Links
from webstore_config.locators import BaseLocators as locators, LocatorType
from webstore_config.config import Config

D = TypeVar("D", bound=WebDriver | WebElement)
T = TypeVar('T')
ConditionType = Callable[[D], T]


class BasePage:
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.url = Links.BASE_URL

    def open(self) -> None:
        with allure.step(f"Открытие страницы по ссылке: {self.url}"):
            self.driver.get(self.url)

    def is_url_same(self, url: str, timeout: float=Config.TIMEOUT) -> bool:
        try:
            return self.find(EC.url_to_be(url), timeout)
        except TimeoutException:
            return False

    def refresh(self) -> None:
        with allure.step(f'Обновление страницы: "{self.__class__.__name__}"'):
            self.driver.refresh()

    def wait_until_not(
            self,
            condition: ConditionType,
            timeout: float=Config.TIMEOUT,
            poll_frequency: float=Config.POLL_FREQUENCY
    ) -> T | Literal[True]:
        with (allure.step(f'Ожидание, пока условие ({condition})'
                         f' не станет ложным')):
            return (
                wait(self.driver, timeout, poll_frequency=poll_frequency)
                .until_not(condition)
            )

    def find(
            self,
            condition: ConditionType,
             timeout: float=Config.TIMEOUT,
            poll_frequency: float=Config.POLL_FREQUENCY
    ) -> T:
        with allure.step(f'Поиск элемента страницы "{self.url}". '
                         f'Условие и локатор: "{condition}"'):
            return (
                wait(self.driver, timeout, poll_frequency=poll_frequency)
                .until(condition)
            )

    def find_visible_element(
            self,
            locator: LocatorType,
            timeout: float=Config.TIMEOUT
    ) -> WebElement | T:
        return self.find(EC.visibility_of_element_located(locator), timeout)

    def find_clickable_element(
            self,
            locator: LocatorType,
            timeout: float=Config.TIMEOUT
    ) -> WebElement | T:
        element = self.find(EC.element_to_be_clickable(locator), timeout)
        self.scroll_to_element(element)
        return element

    def click(self, locator: LocatorType) -> None:
        button = self.find_clickable_element(locator)
        try:
            button.click()
        except (ElementClickInterceptedException, TimeoutException):
            self.driver.execute_script('arguments[0].click()', button)

    def find_presence_element(
            self,
            locator: LocatorType,
            timeout: float = Config.TIMEOUT
    ) -> WebElement | T:
        return self.find(EC.presence_of_element_located(locator), timeout)

    def find_elements(
            self,
            locator: LocatorType,
            timeout: float = Config.TIMEOUT
    ) -> list[WebElement] | T:
        return self.find(
            EC.visibility_of_all_elements_located(locator),
            timeout
        )

    @allure.step('Ожидание изменения значения "value" у элемента')
    def wait_value_change(
            self,
            locator: LocatorType,
            timeout: float = Config.TIMEOUT
    ) -> bool:
        try:
            return self.find(WaitValueChanges(locator), timeout)
        except TimeoutException:
            return False

    @allure.step('Ожидание изменения значения "text" у элемента')
    def wait_text_change(
            self, locator: LocatorType,
            timeout: float = Config.TIMEOUT
    ) -> bool:
        try:
            return self.find(WaitTextChanges(locator), timeout)
        except TimeoutException:
            return False

    def is_attribute_present(
            self,
            locator: LocatorType,
            attribute: str,
            text: str,
            timeout: float = Config.TIMEOUT
    ) -> bool:
        try:
            return self.find(
                EC.text_to_be_present_in_element_attribute(
                    locator,
                    attribute,
                    text
                ),
                timeout
            )
        except TimeoutException:
            return False

    def is_invisible(
            self,
            locator: LocatorType,
            timeout: float = Config.TIMEOUT
    ) -> bool:
        try:
            return self.find(
                EC.invisibility_of_element_located(locator),
                timeout
            )
        except TimeoutException:
            return False

    @allure.step('Прокрутка страницы до искомого элемента')
    def scroll_to_element(self, element: WebElement) -> None:
        self.driver.execute_script(
            "arguments[0].scrollIntoView({behavior: 'instant', "
            "block: 'start', inline: 'start'});",
            element
        )

    @property
    def header(self) -> str | None:
        with allure.step(f'Запрос заголовка страницы: '
                         f'"{self.__class__.__name__}"'):
            try:
                return self.find_visible_element(locators.HEADER).text
            except TimeoutException:
                return None

    @allure.step('Нажатие кнопки навигации (меню)')
    def click_navigation_bar(self) -> None:
        self.find_clickable_element(locators.NAVIGATION_BAR).click()

    @allure.step('Нажатие на заголовок "Магазин"')
    def click_header_button(self) -> None:
        self.find_clickable_element(locators.HEADER_BUTTON).click()

    @allure.step('Нажатие кнопки "Корзинка"')
    def click_cart_button(self) -> None:
        self.find_clickable_element(locators.CART_BUTTON).click()

    @allure.step('Запрос текста заголовка')
    def get_header_text(self) -> str | None:
        try:
            return self.find_visible_element(locators.HEADER_BUTTON).text
        except TimeoutException:
            return None

    @allure.step('Запрос текущего URL страницы')
    def get_current_url(self) -> str:
        return self.driver.current_url