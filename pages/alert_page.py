from selenium.webdriver.common.by import By

from elements.button import Button
from elements.web_element import WebElement
from pages.base_page import BasePage


class AlertPage(BasePage):
    UNIQUE_ELEMENT_LOC = By.ID, "content"
    BUTTON_JS_LOC = "//button[@onclick='{}']"
    JS_ALERT = "jsAlert()"
    JS_CONFIRM = "jsConfirm()"
    JS_PROMPT = "jsPrompt()"
    RESULT_LOC = By.ID, "result"

    def __init__(self, browser):
        super().__init__(browser)
        self.name_page = 'Alert page'
        self.unique_element = WebElement(
            self.browser,
            self.UNIQUE_ELEMENT_LOC,
            description="Alert page -> unique content"
        )
        self.text_result = WebElement(
            self.browser,
            self.RESULT_LOC,
            description="Alert page -> text Result"
        )

    def click_button(self, name_button):
        button = Button(
            self.browser,
            self.BUTTON_JS_LOC.format(name_button),
            description=f"Alert page -> click button: '{name_button}'"
        )
        button.click()

    def click_js_button(self, name_button):
        js_button = Button(
            self.browser,
            self.BUTTON_JS_LOC.format(name_button),
            description=f"Alert page -> click js button: '{name_button}'"
        )
        js_button.js_click()

    def click_alert_button(self) -> None:
        self.click_button(self.JS_ALERT)

    def click_confirm_button(self) -> None:
        self.click_button(self.JS_CONFIRM)

    def click_prompt_button(self) -> None:
        self.click_button(self.JS_PROMPT)

    def click_js_alert_button(self) -> None:
        self.click_js_button(self.JS_ALERT)

    def click_js_confirm_button(self) -> None:
        self.click_js_button(self.JS_CONFIRM)

    def click_js_prompt_button(self) -> None:
        self.click_js_button(self.JS_PROMPT)

    def get_text_result(self) -> str:
        return self.text_result.get_text()
