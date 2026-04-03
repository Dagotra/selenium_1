from browser.browser import Browser
from logger.logger import Logger


class BasePage:
    UNIQUE_ELEMENT_LOC = None

    def __init__(self, browser: Browser) -> None:
        self.browser = browser
        self.name_page = None
        self.unique_element = None
        self.unique_element_file_uploaded = None

    def wait_for_open(self) -> None:
        self.unique_element.wait_for_presence()
        Logger.info(
            f"Страница '{self.name_page}' - успешно открыта, найден уникальный элемент '{self.UNIQUE_ELEMENT_LOC[1]}', "  # noqa
            f"тип элемента: '{self.UNIQUE_ELEMENT_LOC[0]}'"  # noqa
        )


    def __str__(self) -> str:
        return f"{self.__class__.__name__}[{self.name_page}]"

    def __repr__(self) -> str:
        return str(self)
