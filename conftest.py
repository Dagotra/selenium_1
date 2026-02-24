import pytest
from driver_singleton import DriverSingleton


@pytest.fixture
def browser(request):
    driver = DriverSingleton(language=request.param)
    yield driver
    DriverSingleton.close_driver()
