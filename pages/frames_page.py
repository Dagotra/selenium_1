from elements.button import Button
from elements.web_element import WebElement
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class FramesPage(BasePage):
    UNIQUE_ELEMENT_LOC = By.XPATH, "//h1[text()='Frames']"
    NESTED_FRAMES2_LOC = By.ID, "frame2"
    BUTTON_NESTED_FRAME_LOC = By.XPATH, "//span[contains(text(),'Nested Frames')]"
    FRAME_TEXT_LOC = By.XPATH, "//h1"

    def __init__(self, browser):
        super().__init__(browser)
        self.name_page = "Frames page"
        self.unique_element = WebElement(
            self.browser,
            self.UNIQUE_ELEMENT_LOC,
            description="Frames page -> unique element page"
        )
        self.text_frame = WebElement(
            self.browser,
            self.FRAME_TEXT_LOC,
            description="Frame page -> get text Frames"
        )
        self.button_nested_frames = Button(
            self.browser,
            self.BUTTON_NESTED_FRAME_LOC,
            description="Frame page -> open iframe Alerts, Frame & Windows -> click button 'Nested Frames'"
        )

    def click_button_nested_frames(self) -> None:
        self.button_nested_frames.click()

    def get_text_frame(self) -> str:
        return self.text_frame.get_text()

    def wait_and_switch_frame1(self):
        self.browser.wait_and_switch_to_frame("frame1")

    def wait_and_switch_frame2(self):
        self.browser.wait_and_switch_to_frame("frame2")
