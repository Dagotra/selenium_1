from elements.web_element import WebElement
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class NewWindowPage(BasePage):
    UNIQUE_ELEMENT_LOC = By.XPATH, "//body/div[@class='example']/h3"
    TEXT_NEW_TAB_LOC = By.XPATH, "//body/div[@class='example']/h3"

    def __init__(self, browser):
        super().__init__(browser)
        self.name_page = "New window page"
        self.unique_element = WebElement(
            self.browser,
            self.UNIQUE_ELEMENT_LOC,
            description="New window page -> unique element page"
        )
        self.text_new_tab = WebElement(
            self.browser,
            self.TEXT_NEW_TAB_LOC,
            description="New window page -> get text in page"
        )

    def get_text_new_tab(self) -> str:
        self.text_new_tab.click()
        return self.text_new_tab.get_text()
