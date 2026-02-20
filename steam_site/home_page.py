from selenium.webdriver.common.by import By
from selenium_1.steam_site.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class HomePage(BasePage):
    UNIQUE_ELEMENT_LOC = By.ID, 'home_maincap_v7'
    HEADER_LOC = By.XPATH, '//div[@role="navigation"]'
    SEARCH_INPUT = By.XPATH, f'{HEADER_LOC[1]}//input[@type="text"]'
    SEARCH_BUTTON = By.XPATH, f'{HEADER_LOC[1]}//button[@type="submit"]'

    def wait_unique_element(self):
        """Поиск уникального элемента на главной странице"""
        self.wait.until(EC.visibility_of_element_located(self.UNIQUE_ELEMENT_LOC))

    def enter_game_name(self, name):
        """Ввод названия игры в поле поиска"""
        element = self.wait.until(EC.element_to_be_clickable(self.SEARCH_INPUT))
        element.click()
        element.send_keys(name)
        self.wait.until(EC.visibility_of_element_located(self.SEARCH_INPUT))

    def click_search(self):
        """Нажимаем кнопку поиска"""
        element = self.wait.until(EC.element_to_be_clickable(self.SEARCH_BUTTON))
        element.click()
