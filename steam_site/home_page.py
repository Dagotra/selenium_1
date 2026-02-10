from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium_1.steam_site.base_page import BasePage


class HomePage(BasePage):
    HOME_PAGE_URL = "https://store.steampowered.com/"
    UNIQUE_ELEMENT_LOC = By.XPATH, '//*[@id="home_maincap_v7"]'
    HEADER_LOC = By.XPATH, '//div[@role="navigation"]'
    SEARCH_INPUT = By.XPATH, f'{HEADER_LOC[1]}//input[@type="text"]'
    SEARCH_BUTTON = By.XPATH, f'{HEADER_LOC[1]}//button[@type="submit"]'
    SELECT_BUTTON_LANGUAGE = By.XPATH, "//*[@id='language_pulldown']"
    DROPDOWN_LANGUAGE = By.XPATH, "//*[@id='language_dropdown']"
    # Локаторы для конкретных языков
    # RUS_LANGUAGE = By.XPATH, f"{DROPDOWN_LANGUAGE[1]}//a[contains(@onclick, 'russian')]"
    # ENG_LANGUAGE = By.XPATH, f"{DROPDOWN_LANGUAGE[1]}//a[contains(@onclick, 'english')]"
    CHOICE_LANGUAGE = "//a[contains(@onclick, '{}')]"
    LANGUAGE_BAR = By.XPATH, "//div[contains(@class, 'newmodal_header_border')]"

    def open_page(self):
        self.browser.get(self.HOME_PAGE_URL)

    def wait_unique_element(self):
        """Поиск уникального элемента на главной странице"""
        self.wait_visible(self.UNIQUE_ELEMENT_LOC)

    def enter_game_name(self, name):
        """Ввод названия игры в поле поиска"""
        self.click(self.SEARCH_INPUT)
        self.type(self.SEARCH_INPUT, name)

    def click_search(self):
        """Нажимаем кнопку поиска"""
        self.click(self.SEARCH_BUTTON)

    # Метод для выбора конкретного языка
    # def change_language_eng(self):
    #     """Смена языка на английский"""
    #     self.wait_visible(self.SELECT_BUTTON_LANGUAGE)
    #     self.click(self.SELECT_BUTTON_LANGUAGE)
    #     self.wait_visible(self.DROPDOWN_LANGUAGE)
    #     self.click(self.ENG_LANGUAGE)
    #     self.wait_visible(self.LANGUAGE_BAR)
    #     self.wait_not_visible(self.LANGUAGE_BAR)

    def change_language(self, language):
        """Смена языка на главной странице"""
        self.wait_visible(self.SELECT_BUTTON_LANGUAGE)
        self.click(self.SELECT_BUTTON_LANGUAGE)
        self.wait_visible(self.DROPDOWN_LANGUAGE)
        self.click((By.XPATH, self.CHOICE_LANGUAGE.format(language)))
        self.wait_visible(self.LANGUAGE_BAR)
        self.wait_not_visible(self.LANGUAGE_BAR)

    def check_language(self, check_language):
        """
        Проверка языка
        Args:
            Метод проверяет наличие языка в селекте языка, если он есть это значит что страница на другом языке
            и метод ничего не меняет и возвращает False.
            Если его нет значит страница на нужном нам языке и возвращает True
        """
        self.wait_visible(self.SELECT_BUTTON_LANGUAGE)
        self.click(self.SELECT_BUTTON_LANGUAGE)
        self.wait_visible(self.DROPDOWN_LANGUAGE)
        try:
            self.wait_visible_short((By.XPATH, self.CHOICE_LANGUAGE.format(check_language)))
        except TimeoutException:
            self.click(self.SELECT_BUTTON_LANGUAGE)
            return False
        self.change_language(check_language)
        return True
