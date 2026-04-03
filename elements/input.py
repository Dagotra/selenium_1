from selenium.common import WebDriverException
from elements.base_element import BaseElement
from logger.logger import Logger


class Input(BaseElement):
    def clear(self) -> None:
        element = self.wait_for_visible()
        Logger.info(f"{self}: clear")
        try:
            element.clear()
        except WebDriverException as err:
            Logger.error(f"{self}: {err}")
            raise

    def js_clear(self) -> None:
        element = self.wait_for_presence()
        Logger.info(f"{self}: js clear in input: '{element}'")
        self.browser.execute_script("arguments[0].value = ''", element)

    def send_keys(self, keys: str, clear: bool = True) -> None:
        if clear:
            self.clear()
        element = self.wait_for_visible()
        Logger.info(f"{self}: send keys = '{keys}'")
        try:
            element.send_keys(keys)
        except WebDriverException as err:
            Logger.error(f"{self}: {err}")
            raise

    def send_js_keys(self, keys: str, clear: bool = True) -> None:
        if clear:
            self.js_clear()
        element = self.wait_for_presence()
        Logger.info(f"{self}: js send keys = '{keys}'")
        self.browser.execute_script("arguments[0].value='arguments[1]'", element, keys)

    def send_keys_to_hidden_input(self, keys: str) -> None:
        element = self.wait_for_presence()
        Logger.info(f"{self}: send keys from invisibility input = '{keys}'")
        element.send_keys(keys)

    def upload_file(self, file_path: str) -> None:
        Logger.info(f"{self.__class__.__name__}: download file")
        upload_file = self.wait_for_visible()

        Logger.info(f"{self}: upload file = '{file_path}'")
        upload_file.send_keys(file_path)
