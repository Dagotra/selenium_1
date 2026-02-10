from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    TIMEOUT_WEB_DRIVER = 10
    SHORT_TIME_OUT = 1

    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, BasePage.TIMEOUT_WEB_DRIVER)
        self.short_wait = WebDriverWait(browser, BasePage.SHORT_TIME_OUT)

    def build_not_found_message(self, locator):
        by, value = locator
        return f"Элемент '{value}' на странице не найден за '{self.TIMEOUT_WEB_DRIVER}' секунд"

    def wait_visible(self, locator, message=None):
        if message is None:
            message = self.build_not_found_message(locator)
        result = self.wait.until(EC.visibility_of_element_located(locator), message)
        return result

    def build_found_message(self, locator):
        by, value = locator
        return f"Элемент '{value}' не исчез на странице за '{self.TIMEOUT_WEB_DRIVER}' секунд"

    def wait_not_visible(self, locator, message=None):
        if message is None:
            message = self.build_found_message(locator)
        result = self.wait.until(EC.invisibility_of_element_located(locator), message)
        return result

    def type(self, locator, text):
        self.wait.until(EC.element_to_be_clickable(locator)).send_keys(text)

    def click(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator)).click()

    def get_text(self, locator):
        text_element = self.wait.until(EC.visibility_of_element_located(locator))
        return text_element.text

    def get_attribute(self, locator, attribute):
        text_attribute = self.wait.until(EC.visibility_of_element_located(locator))
        return text_attribute.get_attribute(attribute)

    def refresh(self, locator):
        self.browser.refresh()
        self.wait_visible(locator)

    def wait_present_elements(self, locator):
        elements = self.wait.until(EC.presence_of_all_elements_located(locator))
        return elements

    def wait_visible_short(self, locator):
        return self.short_wait.until(EC.visibility_of_element_located(locator))
