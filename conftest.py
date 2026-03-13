import pytest
from browser.browser_factory import BrowserFactory
from logger.logger import Logger


@pytest.fixture(scope="session")
def driver():
    print()
    Logger.info(f"Создаем фикстуру")
    driver = BrowserFactory.get_driver()
    yield driver
    print()
    Logger.info(f"Закрываем вэбдрайвер '{driver.name}' ")
    driver.quit()
    Logger.info("Сессия закрыта")
