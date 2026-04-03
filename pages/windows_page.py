from elements.button import Button
from elements.web_element import WebElement
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class WindowsPage(BasePage):
    UNIQUE_ELEMENT_LOC = By.ID, "content"
    BUTTON_CLICK_HERE_LOC = By.XPATH, "//*[@id='content']//a[@target='_blank']"
    TEXT_TAB_LOC = By.XPATH, "//body/div[contains(@class, 'example')]/h3"

    def __init__(self, browser):
        super().__init__(browser)
        self.name_page = "Interaction page"
        self.unique_element = WebElement(
            self.browser,
            self.UNIQUE_ELEMENT_LOC,
            description="Interaction page -> unique element page"
        )
        self.button_click_here = Button(
            self.browser,
            self.BUTTON_CLICK_HERE_LOC,
            description="Interaction page -> click button 'Click Here'"
        )
        self.text_tab = WebElement(
            self.browser,
            self.TEXT_TAB_LOC,
            description="New window page -> get text in page"
        )

    def click_button_click_here(self) -> None:
        self.button_click_here.click()

    def get_text_tab(self) -> str:
        return self.text_tab.get_text()
