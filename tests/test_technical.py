import time
import pytest

from pages.auth_page import AuthPage
from utils.assertion import AssertValues
from test_data import headers


@pytest.mark.parametrize('driver', ['CHROME', 'FIREFOX'], indirect=True)
class TestTechnical:
    def setup_method(self):
        self.auth_page = AuthPage(self.driver)

    def test_website_launch_by_HTTPS(self):
        self.driver.get("https://91.197.96.80")
        self.auth_page.check_header(headers.AUTH_PAGE)

    def test_website_load_time(self):
        start_time = time.time()
        self.auth_page.open()
        end_time = time.time()
        error_rate = 0.1
        time_of_load_website = end_time-start_time-error_rate
        print(f"{time_of_load_website=}")
        AssertValues.is_smaller_or_equal(
            "Time's load website",
            time_of_load_website,
            3
        )
