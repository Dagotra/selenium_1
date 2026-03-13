from selenium.webdriver.common.by import By
from elements.web_element import WebElement
from pages.base_page import BasePage


class StartPage(BasePage):
    UNIQUE_ELEMENT_LOC = By.ID, "content"
    TEXT_LOCATOR = By.XPATH, '//*[@id="content"]//p'

    def __init__(self, browser):
        super().__init__(browser)
        self.name_page = "Start page"
        self.unique_element = WebElement(
            self.browser,
            self.UNIQUE_ELEMENT_LOC,
            description="Start page -> unique content"
        )
        self.success_message = WebElement(
            self.browser,
            self.TEXT_LOCATOR,
            description="Start page -> success text"
        )

    def get_success_message(self) -> str:
        return self.success_message.get_text()
