from bs4 import BeautifulSoup
from selenium.common import TimeoutException

from browser.browser import Browser
from elements.demo import DemoMulti
from elements.multi_web_element import MultiWebElement
from elements.web_element import WebElement
from logger.logger import Logger
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class InfiniteScrollPage(BasePage):
    UNIQUE_ELEMENT_LOC = By.ID, "content"
    MULTI_ALL_PARAGRAPH_ELEMENT_LOC = '(//div[contains(@class, "jscroll-added")])[{}]'
    LOAD_BAR_LOC = By.XPATH, "//div[contains(@class='jscroll-loading')]//small[contains(text(), 'Loading')]"

    def __init__(self, browser: Browser) -> None:
        super().__init__(browser)
        self.name_page = "Infinity scroll"
        self.unique_element = WebElement(
            self.browser,
            self.UNIQUE_ELEMENT_LOC,
            description="Infinite scroll page -> unique element"
        )
        self.load_bar = WebElement(
            self.browser,
            self.LOAD_BAR_LOC,
            description="Infinite scroll page -> wait visibility/not visibility load bar"
        )
        self.multi_all_element = DemoMulti(
            self.browser,
            self.MULTI_ALL_PARAGRAPH_ELEMENT_LOC,
            description="Infinite scroll page -> scroll one step"
        )

    def scroll_one_step(self):
        last_paragraph = self.multi_all_element.last_element()
        last_paragraph.scroll_into_view()

    def parse_paragraph(self) -> int:
        html = self.browser.get_page_source()
        soup = BeautifulSoup(html, "html.parser")
        rows = soup.find_all("div", class_="jscroll-added")
        return len(rows)

    def scroll_until_age(self, age: int) -> int:
        current = self.parse_paragraph()
        while current < age:
            try:
                self.scroll_one_step()
                current = self.parse_paragraph()
            except TimeoutException as err:
                Logger.error(f"{self}: {err}")
                raise
        return current
