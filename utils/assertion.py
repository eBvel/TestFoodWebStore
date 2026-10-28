import allure

from collections.abc import Sequence
from typing_extensions import TypeVar
from pages.base_page import BasePage

T = TypeVar("T", bound=float | str)
F = TypeVar("F", bound=float)


class Assert:
    @staticmethod
    def compare_values(
            value_name: str,
            current_value: T,
            expected_value: T
    ) -> None:
        arguments: str = f"{value_name}\n{current_value=}\n{expected_value=}"
        with allure.step(f'Проверка:\n{arguments}'):
            print(arguments)
            assert current_value == expected_value, "FAILED: incorrect value."
            print("PASSED: Value is correct.")

    @staticmethod
    def contains(value_name: str, value: T, data: Sequence) -> None:
        arguments: str = f"{value_name}\n{value=}\n{data=}"
        with allure.step(f'Проверка:\n{arguments}'):
            print(arguments)
            assert value in data, "FAILED: value is missing."
            print("PASSED: value is present in the data.")

    @staticmethod
    def is_smaller_or_equal(
            value_name: str,
            current_value: F,
            limit: F
    ) -> None:
        arguments: str = f"{value_name}\n{current_value=}\n{limit=}"
        with allure.step(f'Проверка:\n{arguments}'):
            print(arguments)
            assert current_value <= limit, \
                "FAILED: value is bigger than limit."
            print("PASSED: Value is smaller than or equal to the limit.")

    @staticmethod
    def is_bigger_or_equal(
            value_name: str,
            current_value: F,
            limit: F
    ) -> None:
        arguments: str = f"{value_name}\n{current_value=}\n{limit=}"
        with allure.step(f'Проверка:\n{arguments}'):
            print(arguments)
            assert current_value >= limit, \
                "FAILED: value is smaller than limit."
            print("PASSED: Value is bigger than or equal to the limit.")

    @staticmethod
    def check_header(page: BasePage, expected_header: str) -> None:
        current_header = page.header
        arguments:str = (f"{page.__class__.__name__} - header"
                     f"\n{current_header=}\n{expected_header=}")
        with allure.step(f'Проверка заголовка страницы:\n{arguments}'):
            print(arguments)
            assert current_header == expected_header, \
                'FAILED: incorrect header.'
            print("PASSED: header is correct.")

    @staticmethod
    def check_url(page: BasePage) -> None:
        arguments: str = (f"{page.__class__.__name__} - URL\n"
                     f"current_url={page.get_current_url()}\n"
                     f"expected_url={page.url}")
        with allure.step(f"Проверка URL страницы:\n{arguments}"):
            print(arguments)
            assert page.is_url_same(page.url), 'FAILED: incorrect URL.'
            print('PASSED: URL is correct.')