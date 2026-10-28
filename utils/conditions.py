from selenium.common import StaleElementReferenceException
from selenium.webdriver.remote.webdriver import WebDriver
from typing import Literal

ByType = Literal["id", "xpath", "link text", "partial link text", "name", "tag name", "class name", "css selector"]
LocatorType = tuple[ByType, str]


class WaitValueChanges(object):
    def __init__(self, locator: LocatorType):
        self.locator = locator
        self.value = None

    def __call__(self, driver: WebDriver):
        try:
            element_value = (
                driver
                .find_element(*self.locator)
                .get_attribute('value')
            )
            if not self.value:
                self.value = element_value
            return element_value != self.value
        except (StaleElementReferenceException, ValueError):
            return False


class WaitTextChanges(object):
    def __init__(self, locator: LocatorType):
        self.locator = locator
        self.text = None

    def __call__(self, driver: WebDriver):
        try:
            element_text = driver.find_element(*self.locator).text
            if not self.text:
                self.text = element_text
            return element_text != self.text
        except (StaleElementReferenceException, ValueError):
            return False