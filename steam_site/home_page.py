from selenium.webdriver.common.by import By
from selenium_1.steam_site.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class HomePage(BasePage):
    UNIQUE_ELEMENT_LOC = By.ID, 'home_maincap_v7'
    HEADER_LOC = By.XPATH, '//div[@role="navigation"]'
    SEARCH_INPUT = By.XPATH, f'{HEADER_LOC[1]}//input[@type="text"]'
    SEARCH_BUTTON = By.XPATH, f'{HEADER_LOC[1]}//button[@type="submit"]'
    SELECT_BUTTON_LANGUAGE = By.ID, "language_pulldown"
    DROPDOWN_LANGUAGE = By.ID, "language_dropdown"
    CHOICE_LANGUAGE = "//a[contains(@onclick, '{}')]"
    LANGUAGE_BAR = By.XPATH, "//div[contains(@class, 'newmodal_header_border')]"


    def wait_unique_element(self):
        """Поиск уникального элемента на главной странице"""
        self.wait.until(EC.visibility_of_element_located(self.UNIQUE_ELEMENT_LOC))

    def enter_game_name(self, name):
        """Ввод названия игры в поле поиска"""
        element = self.wait.until(EC.element_to_be_clickable(self.SEARCH_INPUT))
        element.click()
        element.send_keys(name)

    def click_search(self):
        """Нажимаем кнопку поиска"""
        element = self.wait.until(EC.element_to_be_clickable(self.SEARCH_BUTTON))
        element.click()

    def change_language(self, language):
        """Смена языка на главной странице"""
        select_button = self.wait.until(EC.element_to_be_clickable(self.SELECT_BUTTON_LANGUAGE))
        select_button.click()
        language_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.CHOICE_LANGUAGE.format(language))))
        language_button.click()
        self.wait.until(EC.visibility_of_element_located(self.LANGUAGE_BAR))
        self.wait.until(EC.invisibility_of_element_located(self.LANGUAGE_BAR))

    def check_language(self):
        result = self.driver.execute_script("return document.documentElement.lang;")
        return result
