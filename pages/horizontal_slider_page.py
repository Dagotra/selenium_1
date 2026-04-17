from selenium.webdriver.common.by import By
from elements.web_element import WebElement
from pages.base_page import BasePage
from elements.slider_element import SliderElement

from collections import namedtuple

SliderAttributes = namedtuple('SliderAttributes', ['min', 'max', 'step', 'value'])


class HorizontalSliderPage(BasePage):
    UNIQUE_ELEMENT_LOC = By.ID, "content"
    INPUT_RANGE_LOC = By.XPATH, "//input[@type='range']"
    RESULT_TEXT_RANGE_LOC = By.ID, "range"
    MIN_VALUE_ATTRIBUTE = "min"
    MAX_VALUE_ATTRIBUTE = "max"
    VALUE_ATTRIBUTE = "value"
    STEP_VALUE_ATTRIBUTE = "step"

    def __init__(self, browser):
        super().__init__(browser)
        self.name_page = "Horizontal slider"
        self.unique_element = WebElement(
            self.browser,
            self.UNIQUE_ELEMENT_LOC,
            description="Horizontal slider page -> unique element"
        )
        self.text_range = WebElement(
            self.browser,
            self.RESULT_TEXT_RANGE_LOC,
            description="Horizontal slider page -> get text result range"
        )
        self.slider_input = SliderElement(
            self.browser,
            self.INPUT_RANGE_LOC,
            description="Horizontal slider page -> focus slider"
        )

    def get_slider_value_text(self) -> str:
        return f'{float(self.text_range.get_text()):g}'

    def get_values(self) -> SliderAttributes:
        return SliderAttributes(
            min=float(self.slider_input.get_attribute(self.MIN_VALUE_ATTRIBUTE)),
            max=float(self.slider_input.get_attribute(self.MAX_VALUE_ATTRIBUTE)),
            step=float(self.slider_input.get_attribute(self.STEP_VALUE_ATTRIBUTE)),
            value=float(self.slider_input.get_attribute(self.VALUE_ATTRIBUTE))
        )

    def set_slider_value(self, target_value: float) -> str:
        result = self.slider_input.set_value(target_value)
        return f"{result:g}"
