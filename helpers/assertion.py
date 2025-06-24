class Assert:
    @staticmethod
    def assert_equal(actual, expected, message="Values are not equal"):
        assert actual == expected, f"{message}: Expected '{expected}', got '{actual}'"

    @staticmethod
    def assert_not_equal(actual, expected, message="Values are unexpectedly equal"):
        assert actual != expected, f"{message}: Expected value not equal to '{expected}'"

    @staticmethod
    def assert_true(condition, message="Condition is not True"):
        assert condition, message

    @staticmethod
    def assert_false(condition, message="Condition is not False"):
        assert not condition, message

    @staticmethod
    def assert_in(member, container, message="Value not found in container"):
        assert member in container, f"{message}: '{member}' not in '{container}'"

    @staticmethod
    def assert_not_in(member, container, message="Value found in container"):
        assert member not in container, f"{message}: '{member}' found in '{container}'"

    @staticmethod
    def assert_is_none(value, message="Value is not None"):
        assert value is None, message

    @staticmethod
    def assert_is_not_none(value, message="Value is None"):
        assert value is not None, message

    @staticmethod
    def assert_greater(a, b, message="First value is not greater than second"):
        assert a > b, f"{message}: '{a}' is not greater than '{b}'"

    @staticmethod
    def assert_less(a, b, message="First value is not less than second"):
        assert a < b, f"{message}: '{a}' is not less than '{b}'"
