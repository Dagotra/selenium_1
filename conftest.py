import pytest
from selenium_1.driver_singleton import DriverSingleton


@pytest.fixture
def browser(request):
    driver = DriverSingleton()
    lange = request.param
    valid_language = (driver.options.to_capabilities().get('goog:chromeOptions').get('args'))[1]
    if lange not in valid_language:
        DriverSingleton.close_driver()
        driver = DriverSingleton(language=request.param)
    yield driver

    DriverSingleton.close_driver()
