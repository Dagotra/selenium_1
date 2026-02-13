from selenium.webdriver.support.ui import WebDriverWait
from selenium_1.config.config_reader import ConfigReader
from selenium_1.driver_singleton import DriverSingleton


class BasePage:
    config = ConfigReader()
    TIME_OUT_WEB_DRIVER = config.get("timeout", "default")
    SHORT_TIME_OUT = config.get("timeout", "short")

    def __init__(self):
        self.driver = DriverSingleton()
        self.wait = WebDriverWait(self.driver, BasePage.TIME_OUT_WEB_DRIVER)
        self.short_wait = WebDriverWait(self.driver, BasePage.SHORT_TIME_OUT)
