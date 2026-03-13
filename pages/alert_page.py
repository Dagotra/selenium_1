from selenium.webdriver.common.by import By

from elements.button import Button
from elements.web_element import WebElement
from pages.base_page import BasePage


class AlertPage(BasePage):
    UNIQUE_ELEMENT_LOC = By.ID, "content"
    BUTTON_JS_ALERT_LOC = By.XPATH, "//button[@onclick='jsAlert()']"
    BUTTON_JS_CONFIRM_LOC = By.XPATH, "//button[@onclick='jsConfirm()']"
    BUTTON_JS_PROMPT_LOC = By.XPATH, "//button[@onclick='jsPrompt()']"
    RESULT_LOC = By.ID, "result"

    def __init__(self, browser):
        super().__init__(browser)
        self.name_page = 'Alert page'
        self.unique_element = WebElement(
            self.browser,
            self.UNIQUE_ELEMENT_LOC,
            description="Alert page -> unique content"
        )
        self.js_alert = Button(
            self.browser,
            self.BUTTON_JS_ALERT_LOC,
            description="Alert page -> click js alert button"
        )
        self.js_confirm = Button(
            self.browser,
            self.BUTTON_JS_CONFIRM_LOC,
            description="Alert page -> click js confirm button"
        )
        self.js_prompt = Button(
            self.browser,
            self.BUTTON_JS_PROMPT_LOC,
            description="Alert page -> click js prompt button"
        )
        self.text_result = WebElement(
            self.browser,
            self.RESULT_LOC,
            description="Alert page -> text Result"
        )

    def get_js_alert_text(self) -> str:
        self.js_alert.click()
        return self.browser.get_alert_text()

    def get_js_confirm_text(self) -> str:
        self.js_confirm.click()
        return self.browser.get_alert_text()

    def get_js_prompt_text(self) -> str:
        self.js_prompt.click()
        return self.browser.get_alert_text()

    def get_js_method_alert_text(self) -> str:
        self.js_alert.js_click()
        return self.browser.get_alert_text()

    def get_js_method_confirm_text(self) -> str:
        self.js_confirm.js_click()
        return self.browser.get_alert_text()

    def get_js_method_prompt_text(self) -> str:
        self.js_prompt.js_click()
        return self.browser.get_alert_text()

    def get_text_result(self) -> str:
        return self.text_result.get_text()
