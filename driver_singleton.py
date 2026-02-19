from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium_1.config.config_reader import ConfigReader


class DriverSingleton:
    _driver = None

    def __new__(cls, language="ru", *args, **kwargs):
        if cls._driver is None:
            config = ConfigReader()
            options = Options()
            options.add_argument(config.get("browser", "arguments"))
            options.add_argument(f"--lang={language}")
            cls._driver = webdriver.Chrome(options=options)
        return cls._driver

    @classmethod
    def close_driver(cls):
        if cls._driver:
            cls._driver.quit()
            cls._driver = None
