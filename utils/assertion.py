

class Assert:
    @staticmethod
    def compare_values(value_name, current_value, expected_value):
        print(f"{value_name}\n{current_value=}\n{expected_value=}")
        assert current_value == expected_value, "FAILED: incorrect value."
        print("PASSED: Value is correct.")

    @staticmethod
    def contains(value_name, value, data):
        print(f"{value_name}\n{value=}\n{data=}")
        assert value in data, "FAILED: value is missing."
        print("PASSED: value is present in the data.")

    @staticmethod
    def is_smaller_or_equal(value_name, current_value, limit):
        print(f"{value_name}\n{current_value=}\n{limit=}")
        assert current_value <= limit, "FAILED: value is bigger than limit."
        print("PASSED: Value is smaller than or equal to the limit.")

    @staticmethod
    def is_bigger_or_equal(value_name, current_value, limit):
        print(f"{value_name}\n{current_value=}\n{limit=}")
        assert current_value >= limit, "FAILED: value is smaller than limit."
        print("PASSED: Value is bigger than or equal to the limit.")

    @staticmethod
    def check_header(page, expected_header):
        current_header = page.header
        print(
            f"{page.__class__.__name__} - header"
            f"\n{current_header=}\n{expected_header=}"
        )
        assert page.header == expected_header, 'FAILED: incorrect header.'
        print("PASSED: header is correct.")

    @staticmethod
    def check_url(page):
        print(
            f"{page.__class__.__name__} - URL\n"
            f"current_url={page.get_current_url()}\nexpected_url={page.url}"
        )
        assert page.is_url_same(page.url), 'FAILED: incorrect URL.'
        print('PASSED: URL is correct.')