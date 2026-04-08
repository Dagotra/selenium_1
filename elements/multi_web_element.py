from browser.browser import Browser
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from elements.web_element import WebElement
from logger.logger import Logger


class MultiWebElement:
    DEFAULT_TIME = 0.5

    def __init__(
            self,
            browser: Browser,
            locator: str | tuple[str, str],
            description: str = None,
            timeout: int = None
    ) -> None:
        self.browser = browser
        self.locator = locator
        self.timeout = timeout if timeout is not None else self.DEFAULT_TIME
        self.description = description if description else self.locator.format("'i'")
        self._wait = WebDriverWait(self.browser.driver, timeout=self.timeout)
        self.by = By.XPATH

    def _build_locator(self, index: int) -> tuple[str, str]:
        return self.by, self.locator.format(index)

    def wait_visibly_by_index(self, index: int):
        locator = self._build_locator(index)
        return self._wait.until(expected_conditions.visibility_of_element_located(locator))

    def wait_for_visible_all_elements(self) -> list[WebElement]:
        return self._wait.until(expected_conditions.visibility_of_all_elements_located(self.locator))

    def __str__(self) -> str:
        return f"{self.__class__.__name__}[{self.description}]"

    def __repr__(self) -> str:
        return str(self)

    def _wait_for(self, expected_condition) -> WebElement:
        try:
            Logger.info(f"{self}: wait for '{expected_condition.__name__}'")
            element = self._wait.until(method=expected_condition(self.locator))
            return element
        except TimeoutException as err:
            Logger.error(f"{self}: {err}")
            raise

    def get_quantity_visibly_elements(self) -> int:
        count = 1
        while True:
            try:
                self.wait_visibly_by_index(count)
                count += 1
            except TimeoutException:
                Logger.info(f"{self}: get quantity visibly elements: '{count - 1}'")
                return count - 1

    def scroll_into_view(self, index_element) -> None:
        element = self.wait_visibly_by_index(index_element)
        self.browser.execute_script("arguments[0].scrollIntoView();", element)
