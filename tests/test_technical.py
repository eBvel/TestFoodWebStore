import time
import allure

from pages.auth_page import AuthPage
from utils.assertion import AssertValues
from tests.test_data.pages_data import TechnicalData, AuthData


class TestTechnical:
    @classmethod
    def setup_class(cls):
        cls.auth_page = AuthPage(cls.driver)

    @allure.feature('SECURE CONNECTION')
    @allure.story('Проверка подключения по HTTPS протоколу')
    def test_website_launch_by_https(self):
        self.driver.get(TechnicalData.HTTPS_URL)

        self.auth_page.check_header(AuthData.HEADER)

    @allure.feature('TIME OF LOAD SITE')
    @allure.story('Проверка времени загрузки сайта')
    def test_website_load_time(self):
        start_time = time.time()
        self.auth_page.open()
        end_time = time.time()

        error_rate = 0.1
        time_of_load_website = end_time-start_time-error_rate

        AssertValues.is_smaller_or_equal(
            "TECHNICAL: Time's load website",
            time_of_load_website,
            TechnicalData.MAX_TIME_OF_LOAD_WEBSITE
        )
