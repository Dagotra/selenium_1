from elements.web_element import WebElement
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class HoversPage(BasePage):
    UNIQUE_ELEMENT_LOC = By.ID, "content"
    USER_FIGURE_LOC = "(//div[contains(@class, 'figure')])[{}]"
    FIGCAPTION_LOC = "//div[contains(@class, 'figcaption')]"
    TEXT_USER_LOC = f"({FIGCAPTION_LOC}//h5)[{{}}]"
    LINK_VIEW_USER_LOC = f"({FIGCAPTION_LOC}//a)[{{}}]"

    def __init__(self, browser):
        super().__init__(browser)
        self.name_page = "Hovers"
        self.unique_element = WebElement(
            self.browser,
            self.UNIQUE_ELEMENT_LOC,
            description="Hovers page -> unique element"
        )

    def hover_user(self, index: int) -> None:
        move_to_element_user = WebElement(
            self.browser,
            self.USER_FIGURE_LOC.format(index),
            description=f"Hovers page -> hover user {index}"
        )
        move_to_element_user.move_to_element()

    def get_text_in_hover_user(self, index: int) -> str:
        text_in_user = WebElement(
            self.browser,
            self.TEXT_USER_LOC.format(index),
            description=f"Hovers page -> hover user '{index}' -> get text in 'user{index}'"
        )
        return text_in_user.get_text()

    def click_view_profile_user(self, index: int) -> None:
        button_view_profile_user = WebElement(
            self.browser,
            self.LINK_VIEW_USER_LOC.format(index),
            description=f"Hovers page -> hover user '{index}' -> click user {index} view profile"
        )
        button_view_profile_user.click()
