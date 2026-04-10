from bs4 import BeautifulSoup
from selenium.common import TimeoutException
from browser.browser import Browser
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
        self.load_bar = WebElement(  # в дальнейшем может пригодиться
            self.browser,
            self.LOAD_BAR_LOC,
            description="Infinite scroll page -> wait visibility/not visibility load bar"
        )
        self.list_web_elements = MultiWebElement(
            self.browser,
            self.MULTI_ALL_PARAGRAPH_ELEMENT_LOC,
            description="Infinite scroll page -> checking visible elements",
        )

    def get_list_web_elements(self) -> list[WebElement]:
        list_element = []
        for index, web_element in enumerate(self.list_web_elements):
            list_element.append(web_element)

        Logger.info(f"Get list WebElements: {list_element}")
        return list_element

    def scroll_last_visibly_web_element(self) -> None:
        last_element = self.get_list_web_elements()[-1]
        last_element.scroll_into_view()

    def parse_paragraph(self) -> int:
        html = self.browser.get_page_source()
        soup = BeautifulSoup(html, "html.parser")
        rows = soup.find_all("div", class_="jscroll-added")
        return len(rows)

    def scroll_until_age(self, age: int) -> int:
        current = self.parse_paragraph()
        while current < age:
            try:
                self.scroll_last_visibly_web_element()
                current = self.parse_paragraph()
            except TimeoutException as err:
                Logger.error(f"{self}: {err}")
                raise
        return current
