from elements.button import Button
from elements.web_element import WebElement
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class InteractionsPage(BasePage):
    UNIQUE_ELEMENT_LOC = By.ID, "content"
    BUTTON_CLICK_HERE_LOC = By.XPATH, "//*[@id='content']//a[@target='_blank']"

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

    def click_button_click_here(self) -> None:
        self.button_click_here.click()
