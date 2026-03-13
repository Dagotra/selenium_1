import random
from selenium.webdriver.common.by import By
from elements.input import Input
from elements.web_element import WebElement
from pages.base_page import BasePage


class HorizontalSliderPage(BasePage):
    UNIQUE_ELEMENT_LOC = By.ID, "content"
    INPUT_RANGE_LOC = By.XPATH, "//input[@type='range']"
    RESULT_TEXT_RANGE_LOC = By.ID, "range"
    MIN_VALUE = "min"
    MAX_VALUE = "max"
    STEP_VALUE = "step"

    def __init__(self, browser):
        super().__init__(browser)
        self.name_page = "Horizontal slider"
        self.unique_element = WebElement(
            self.browser,
            self.UNIQUE_ELEMENT_LOC,
            description="Horizontal slider page -> unique element"
        )
        self.slider_input = Input(
            self.browser,
            self.INPUT_RANGE_LOC,
            description="Horizontal slider page -> click slider"
        )
        self.text_range = WebElement(
            self.browser,
            self.RESULT_TEXT_RANGE_LOC,
            description="Horizontal slider page -> get text result range"
        )

    def set_random_slider_value(self) -> str:
        min_value = float(self.slider_input.get_attribute("min"))
        max_value = float(self.slider_input.get_attribute("max"))
        one_number = random.randint(int(min_value) * 2 + 1, int(max_value) * 2 - 1)
        result = one_number / 2
        self.slider_input.js_focus()
        self.slider_input.move_slider_to_value(result)
        return str(result)

    def get_slider_value_text(self) -> str:
        return str(float(self.text_range.get_text()))
