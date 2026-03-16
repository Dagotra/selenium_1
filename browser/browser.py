from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common import WebDriverException
from selenium.webdriver.remote.switch_to import SwitchTo
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from logger.logger import Logger


class Browser:
    DEFAULT_TIMEOUT = 10
    PAGE_LOAD_TIMEOUT = 60

    def __init__(self, driver: WebDriver):
        self._driver = driver
        self._driver.set_page_load_timeout(self.PAGE_LOAD_TIMEOUT)
        self._wait = WebDriverWait(self._driver, self.DEFAULT_TIMEOUT)
        self._switch_to_alert = SwitchTo(self._driver)
        self._action_chains = ActionChains(self._driver)

    @property
    def driver(self):
        return self._driver

    def get(self, url) -> None:
        Logger.info(f"{self}: получаем ссылку '{url}'")
        try:
            self._driver.get(url)
        except WebDriverException as err:
            Logger.error(f"{self}: {err}")
            raise

    def refresh(self):
        self._driver.refresh()

    def close(self):
        self._driver.close()

    def quit(self):
        self._driver.quit()

    def get_alert_text(self) -> str:
        self.switch_to_alert()
        Logger.info(f"{self.__class__.__name__}: get alert text")
        text = self._switch_to_alert.alert.text
        Logger.info(f"Getting the text: '{text}'")
        return text

    def switch_to_alert(self):
        self._wait.until(EC.alert_is_present())
        Logger.info(f"{self.__class__.__name__}: switch to alert")
        alert = self._switch_to_alert.alert
        return alert

    def close_alert(self) -> None:
        Logger.info(f"{self.__class__.__name__}: close alert")
        alert = self.switch_to_alert()
        try:
            alert.accept()
        except WebDriverException as err:
            Logger.error(f"{self}: {err}")
            raise

    def send_keys_in_alert(self, text: str) -> None:
        Logger.info(f"{self.__class__.__name__}: send keys in alert")
        alert = self.switch_to_alert()
        try:
            alert.send_keys(text)
        except WebDriverException as err:
            Logger.error(f"{self}: {err}")
            raise

    def wait_visibility(self, locator) -> None:
        self._wait.until(EC.visibility_of_element_located(locator))

    def get_text_from_element(self, locator) -> str:
        text = self._wait.until(EC.visibility_of_element_located(locator))
        return text.text

    def execute_script(self, script: str, *args) -> None:
        Logger.info(f"{self.__class__.__name__}: execute script = '{script}' with args = '{args}'")
        try:
            self._driver.execute_script(script, *args)
        except TimeoutException as err:
            Logger.error(f"{self}: {err}")
            raise

    def go_back_to_previous_page(self) -> None:
        Logger.info(f"{self.__class__.__name__}: go back to the previous page")
        self._driver.back()

    def get_current_url(self) -> str:
        Logger.info(f"{self.__class__.__name__}: get current url")
        get_url = self._driver.current_url
        Logger.info(f"Received url: '{get_url}'")
        return get_url

    def get_list_tab_window(self) -> list[str]:
        Logger.info(f"{self.__class__.__name__}: get list tab window")
        return self._driver.window_handles

    def switch_to_first_tab(self) -> None:
        Logger.info(f"{self.__class__.__name__}: switch to first tab")
        first_tab = (self.get_list_tab_window())[0]
        self._driver.switch_to.window(first_tab)

    def switch_to_any_tab(self, number_tab) -> None:
        Logger.info(f"{self.__class__.__name__}: switch to any tab")
        any_tab = (self.get_list_tab_window())[number_tab - 1]
        Logger.info(f"{self.__class__.__name__}: switched to '{number_tab}' tab")
        self._driver.switch_to.window(any_tab)

    def switch_to_last_tab(self) -> None:
        Logger.info(f"{self.__class__.__name__}: switch to last tab")
        last_tab = (self.get_list_tab_window())[-1]
        self._driver.switch_to.window(last_tab)

    def get_name_title(self) -> str:
        Logger.info(f"{self.__class__.__name__}: get name title")
        return self._driver.title

    def close_tab(self) -> None:
        Logger.info(f"{self.__class__.__name__}: close tab")
        self._driver.close()
        Logger.info(f"Current tab is closed")

    def wait_for_url_to_be(self, url: str) -> None:
        self._wait.until(EC.url_to_be(url))

    def default_content(self) -> None:
        self._driver.switch_to.default_content()

    def wait_and_switch_to_frame(self, locator) -> None:
        self._wait.until(EC.frame_to_be_available_and_switch_to_it(locator))
