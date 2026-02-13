import pytest
from selenium_1.driver_singleton import DriverSingleton


@pytest.fixture()
def browser():
    driver = DriverSingleton()
    yield driver
    DriverSingleton.close_driver()
