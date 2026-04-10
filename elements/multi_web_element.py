from elements.web_element import WebElement
from browser.browser import Browser


class MultiWebElement:
    DEFAULT_TIME = 10

    def __init__(
            self,
            browser: Browser,
            formattable_xpath: str,
            description: str = None,
            timeout: int | float = None
    ) -> None:
        self.index = 1
        self.browser = browser
        self.formattable_xpath = formattable_xpath
        self.description = description if description else formattable_xpath.format("'i'")
        self.timeout = timeout if timeout is not None else self.DEFAULT_TIME

    def __iter__(self):
        self.index = 1
        return self

    def __next__(self) -> WebElement | None:
        current_element = WebElement(
            self.browser,
            self.formattable_xpath.format(self.index),
            f"{self.description}:[{self.index}]",
            timeout=0.2
        )
        if not current_element.is_exists():
            raise StopIteration
        else:
            self.index += 1
            return current_element

    def __str__(self) -> str:
        return f"{self.__class__.__name__}[{self.description}]"

    def __repr__(self) -> str:
        return str(self)
