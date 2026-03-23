from elements.web_element import WebElement
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class DynamicContentPage(BasePage):
    UNIQUE_ELEMENT_LOC = By.ID, "content"
    IMAGE1_LOC = "(//div[contains(@class, 'large')]//img)[{}]"

    def __init__(self, browser):
        super().__init__(browser)
        self.name_page = "Dynamic content page"
        self.unique_element = WebElement(
            self.browser,
            self.UNIQUE_ELEMENT_LOC,
            description="Dynamic content page -> unique element page"
        )

    def get_img_path(self, number: int, attribute: str = "src") -> str:
        path_img = WebElement(
            self.browser,
            self.IMAGE1_LOC.format(number),
            description=f"Dynamic content page -> get path img № {number}"
        )
        result = path_img.get_attribute(attribute)
        return result

    def get_list_image_paths(self, number_pictures: int) -> list[str]:
        list_img = []
        for i in range(number_pictures):
            path_img = self.get_img_path(i + 1)
            list_img.append(path_img)
        return list_img
