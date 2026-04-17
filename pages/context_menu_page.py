from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from elements.web_element import WebElement


class ContextMenuPage(BasePage):
    UNIQUE_ELEMENT_LOC = By.ID, "content"
    HOT_SPOT_LOC = By.ID, "hot-spot"
    DEMO = By.XPATH, "//div[@oncontextmenu='displayMessage()']"

    def __init__(self, browser):
        super().__init__(browser)
        self.name_page = 'Context menu'
        self.unique_element = WebElement(
            self.browser,
            self.UNIQUE_ELEMENT_LOC,
            description="Context menu page -> unique content"
        )
        self.context_loc = WebElement(
            self.browser,
            self.HOT_SPOT_LOC,
            description="Context menu page -> hot spot element"
        )

    def get_text_alert(self) -> str:
        self.context_loc.click_right_button_mouse()
        return self.browser.get_alert_text()
