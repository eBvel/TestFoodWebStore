from selenium.common import StaleElementReferenceException


class WaitValueChanges(object):
    def __init__(self, locator):
        self.locator = locator
        self.value = None

    def __call__(self, driver):
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
    def __init__(self, locator):
        self.locator = locator
        self.text = None

    def __call__(self, driver):
        try:
            element_text = driver.find_element(*self.locator).text
            if not self.text:
                self.text = element_text
            return element_text != self.text
        except (StaleElementReferenceException, ValueError):
            return False