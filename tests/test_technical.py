import time
import allure

from pytest import mark
from pages.auth_page import AuthPage
from utils.assertion import Assert
from tests.test_data.pages_data import TechnicalData, AuthData


class TestTechnical:
    @classmethod
    def setup_class(cls):
        cls.auth_page = AuthPage(cls.driver)

    @allure.feature('CONNECTION')
    @allure.story('Проверка подключения по HTTPS протоколу')
    @mark.smoke
    def test_website_launch_by_https(self):
        self.driver.get(TechnicalData.HTTPS_URL)

        Assert.check_header(self.auth_page, AuthData.HEADER)

    @allure.feature('CONNECTION')
    @allure.story('Проверка времени загрузки сайта')
    def test_website_load_time(self):
        start_time = time.time()
        self.auth_page.open()
        end_time = time.time()

        error_rate = 0.1
        time_of_load_website = end_time-start_time-error_rate

        Assert.is_smaller_or_equal(
            value_name="Time's load website",
            current_value=time_of_load_website,
            limit=TechnicalData.MAX_TIME_OF_LOAD_WEBSITE
        )
