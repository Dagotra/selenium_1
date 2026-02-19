import pytest
from selenium_1.driver_singleton import DriverSingleton


@pytest.fixture
def browser(request):
    driver = DriverSingleton(language=request.param)
    yield driver
    DriverSingleton.close_driver()
