class SoftAssert:
    def __init__(self):
        self._error = []

    def assert_not_none(self, value, msg=""):
        if value is None:
            self._error.append(f"Expected is not None, but got None. {msg}")

    def assert_equal(self, actual, expected, msg=""):
        if actual != expected:
            self._error.append(f"Expected: '{expected}', got actual: '{actual}'. {msg}")

    def assert_range(self, value, min_value, max_value, msg=""):
        if not min_value <= value <= max_value:
            self._error.append(f"Value: {value} out of range [{min_value}, {max_value}]. {msg}")

    def check(self):
        if self._error:
            raise AttributeError("\n".join(self._error))