from selenium.webdriver.common.by import By

from elements.button import Button
from elements.web_element import WebElement
from pages.base_page import BasePage


class NestedFramesPage(BasePage):
    UNIQUE_ELEMENT_LOC = By.XPATH, "//h1[text()='Nested Frames']"
    BUTTON_FRAMES_FRAME_LOC = By.XPATH, "//span[text()='Frames']"
    NESTED_CHILD_FRAME_LOC = By.XPATH, "//iframe[@srcdoc='<p>Child Iframe</p>']"
    IFRAME_TEXT_LOC = By.XPATH, "//p"
    PARENT_FRAME_TEXT_LOC = By.XPATH, "//body"

    def __init__(self, browser):
        super().__init__(browser)
        self.name_page = "Nested Frames page"
        self.unique_element = WebElement(
            self.browser,
            self.UNIQUE_ELEMENT_LOC,
            description="Nested Frames page -> unique element page"
        )
        self.button_frames = Button(
            self.browser,
            self.BUTTON_FRAMES_FRAME_LOC,
            description="Nested Frames page -> click button 'Frames'"
        )
        self.text_iframe = WebElement(
            self.browser,
            self.IFRAME_TEXT_LOC,
            description="Nested Frames page -> get child iframe text"
        )
        self.text_parent_frame = WebElement(
            self.browser,
            self.PARENT_FRAME_TEXT_LOC,
            description="Nested Frames page -> get parent frame text"
        )

    def click_button_frames(self) -> None:
        self.button_frames.click()

    def get_text_iframe(self) -> str:
        return self.text_iframe.get_text()

    def get_parent_frame_text(self) -> str:
        return self.text_parent_frame.get_text()

    def wait_and_switch_to_frame1(self) -> None:
        self.browser.wait_and_switch_to_frame("frame1")

    def wait_and_switch_to_child_iframe(self) -> None:
        self.browser.wait_and_switch_to_frame(self.NESTED_CHILD_FRAME_LOC)
