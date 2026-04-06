

class AssertValues:
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