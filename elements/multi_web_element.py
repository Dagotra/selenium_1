from browser.browser import Browser


class MultiWebElement:
    DEFAULT_TIME = 10

    def __init__(
            self,
            browser: Browser,
            formattable_xpath: str,
            description: str = None,
            timeout: int = None
    ) -> None:
        self.index = 1
        self.browser = browser
        self.formattable_xpath = formattable_xpath
        self.timeout = timeout if timeout is not None else self.DEFAULT_TIME
        self.description = description if description else self.formattable_xpath.format("'i'")
