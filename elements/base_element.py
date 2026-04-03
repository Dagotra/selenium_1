from selenium.common import WebDriverException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver import ActionChains
from browser.browser import Browser
from logger.logger import Logger


class BaseElement:
    DEFAULT_TIME = 10
    Locator = tuple[str, str]

    def __init__(
            self,
            browser: Browser,
            locator: str | Locator,
            description: str = None,
            timeout: int = DEFAULT_TIME
    ) -> None:
        self.browser = browser
        self.timeout = timeout
        if isinstance(locator, str):
            if "/" in locator:
                self.locator = (By.XPATH, locator)
            else:
                self.locator = (By.ID, locator)
        else:
            self.locator = locator
        self.description = description if description else str(locator)
        self._wait = WebDriverWait(self.browser.driver, timeout=self.timeout)
        self._action_chains = ActionChains(self.browser.driver)

    def __str__(self) -> str:
        return f"{self.__class__.__name__}[{self.description}]"

    def __repr__(self) -> str:
        return str(self)

    def _wait_for(self, expected_condition) -> WebElement:
        try:
            Logger.info(f"{self}: wait for {expected_condition.__name__}")
            element = self._wait.until(method=expected_condition(self.locator))
            return element
        except TimeoutException as err:
            Logger.error(f"{self}: {err}")
            raise

    def _wait_for_not(self, expected_condition) -> None:
        try:
            Logger.info(f"{self}: wait for not {expected_condition.__name__}")
            self._wait.until_not(method=expected_condition(self.locator))
        except TimeoutException as err:
            Logger.error(f"{self}: {err}")
            raise

    def wait_for_presence(self) -> WebElement:
        return self._wait_for(expected_condition=expected_conditions.presence_of_element_located)

    def wait_for_clickable(self) -> WebElement:
        return self._wait_for(expected_condition=expected_conditions.element_to_be_clickable)

    def wait_for_visible(self) -> WebElement:
        return self._wait_for(expected_condition=expected_conditions.visibility_of_element_located)

    def wait_for_not_visible(self) -> None:
        self._wait_for_not(expected_condition=expected_conditions.visibility_of_element_located)

    def wait_for_visible_all_elements(self) -> list[WebElement]:
        return self._wait.until(expected_conditions.visibility_of_all_elements_located(self.locator))

    def is_exists(self) -> bool:
        try:
            self.wait_for_presence()
            return True
        except TimeoutException:
            return False

    def click(self) -> None:
        element = self.wait_for_clickable()
        Logger.info(f"{self}: click")
        try:
            element.click()
        except WebDriverException as err:
            Logger.error(f"{self}: {err}")
            raise

    def js_click(self) -> None:
        element = self.wait_for_presence()
        Logger.info(f"{self}: js click")
        self.browser.execute_script("arguments[0].click();", element)

    def js_focus(self) -> None:
        element = self.wait_for_presence()
        Logger.info(f"{self}: js focus in element: '{element}'")
        self.browser.execute_script("arguments[0].focus()", element)

    def get_text(self) -> str:
        element = self.wait_for_presence()
        Logger.info(f"{self}: берём текст")
        try:
            text = element.text
        except WebDriverException as err:
            Logger.error(f"{self}: {err}")
            raise
        Logger.info(f"{self}: полученный текст = '{text}'")
        return text

    def get_attribute(self, attribute: str) -> str:
        element = self.wait_for_presence()
        Logger.info(f"{self}: get attribute {attribute}")
        try:
            value = element.get_attribute(attribute)
        except WebDriverException as err:
            Logger.error(f"{self}: {err}")
            raise
        Logger.info(f"{self}: attribute '{attribute}' = '{value}'")
        return value

    def click_right_button_mouse(self) -> None:
        element = self.wait_for_clickable()
        Logger.info(f"{self}: {self.__class__.__name__}: click right button in element: {element}")
        try:
            self._action_chains.context_click(element).perform()
        except WebDriverException as err:
            Logger.error(f"{self}: {err}")
            raise

    def move_to_element(self) -> None:
        element = self.wait_for_visible()
        Logger.info(f"{self}: {self.__class__.__name__}: move to element: {element}")
        try:
            self._action_chains.move_to_element(element).perform()
        except WebDriverException as err:
            Logger.error(f"{self}: {err}")
            raise
