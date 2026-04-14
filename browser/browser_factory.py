import os
from enum import StrEnum
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from config.config_reader import ConfigReader
from selenium.webdriver.chrome.options import Options
from logger.logger import Logger


class AvailableNameDriver(StrEnum):
    CHROME = "chrome"


class BrowserFactory:
    @staticmethod
    def get_driver(driver_name=AvailableNameDriver.CHROME) -> WebDriver:
        config = ConfigReader()
        options = Options()
        headless = config.get("browser", "headless")
        if headless:
            options.add_argument("--headless=new")

        if os.path.exists("/.dockerenv"):
            get_argument = config.get("browser", "arguments")
            for argument in get_argument:
                options.add_argument(argument)

            options.binary_location = "/usr/bin/chromium"
        else:
            options.add_argument(config.get("browser", "window_size"))

        Logger.info(f"Создаем вебдрайвер '{driver_name}' c опциями '{options.arguments}'")
        driver = webdriver.Chrome(options=options)
        return driver
