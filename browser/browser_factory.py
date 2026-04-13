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
        options.add_argument(config.get("browser", "arguments"))
        headless = config.get("browser", "headless")
        if headless:
            options.add_argument("--headless=new")
        if os.path.exists("/.dockerenv"):
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.binary_location = "/usr/bin/chromium"
        Logger.info(f"Создаем вебдрайвер '{driver_name}' c опциями '{options.arguments}'")
        driver = webdriver.Chrome(options=options)
        return driver
