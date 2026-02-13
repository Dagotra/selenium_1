from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium_1.steam_site.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class SearchGamePage(BasePage):
    UNIQUE_ELEMENT_LOC = By.XPATH, "//body[contains(@class, 'search_page')]"
    SORT_SELECTOR = By.ID, "sort_by_dselect_container"
    BUTTON_SEARCH_WITH_GAME_TEXT = By.XPATH, ("//div[@id='searchtag_tmpl' "
                                              "and not(contains(@style,'display: none'))]"
                                              "//span[contains(@class,'label')]")
    DROPLIST_SORT = By.XPATH, "//*[@id='sort_by_droplist']"
    DESC_PRICE_BUTTON = By.XPATH, f"{DROPLIST_SORT[1]}//a[@id='Price_DESC']"
    PRICE_GAME = "(//div[contains(@class, 'search_discount_and_price')]//div[@data-price-final])[{}]"
    ATTRIBUTE_PRICE = "data-price-final"
    PRICE_LOCATOR = By.XPATH, "//div[contains(@class,'discount_block') and @data-price-final]"
    DYNAMIC_LOC_NAME_GAME = "(//a[contains(@href, 'app')]//span[@class='title'])[{}]"
    SCROLL_ELEMENT = By.XPATH, "(//div[@data-price-final])[last()]"
    LOAD_BAR = By.ID, "search_results_loading"

    def open_page(self):
        """
        Проверка открытия страницы, наличием уникального локатора на странице
        """
        self.wait.until(EC.visibility_of_element_located(self.UNIQUE_ELEMENT_LOC))

    def check_open_page(self):
        """
        Проверка, что поиск именно данной игры.
        """
        text_game = self.wait.until(EC.visibility_of_element_located(self.BUTTON_SEARCH_WITH_GAME_TEXT)).text.strip()
        if text_game.startswith('"') and text_game.endswith('"'):
            text_game = text_game[1:-1]
        return text_game

    def sort_descending_order(self):
        """
        Выставление сортировки по убыванию
        """
        sort_selector = self.wait.until(EC.element_to_be_clickable(self.SORT_SELECTOR))
        sort_selector.click()
        price_button = self.wait.until(EC.visibility_of_element_located(self.DESC_PRICE_BUTTON))
        price_button.click()

    def get_price_game(self, index):
        price = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.PRICE_GAME.format(index))))
        return price.get_attribute(self.ATTRIBUTE_PRICE)

    def create_list_game(self, index):
        name_game = self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, self.DYNAMIC_LOC_NAME_GAME.format(index)
                 )
            )
        ).text
        return name_game

    def refresh_locator(self):
        self.driver.refresh()
        self.wait.until(EC.visibility_of_element_located(self.UNIQUE_ELEMENT_LOC))

    def get_prices(self):
        """Проверка сортировки в search_page списка всех игр по убыванию цены"""
        self.scroll_list_down()
        elements = self.wait.until(EC.presence_of_all_elements_located(self.PRICE_LOCATOR))
        prices = []
        for i in range(1, len(elements) + 1):
            raw = self.get_price_game(i)
            prices.append(int(raw) if raw and raw.isdigit() else 0)
        return prices

    def scroll_list_down(self):
        """Метод скроллинга по списку отсортированных игр по убыванию до последней игры с ценой"""
        while True:
            elements = self.wait.until(EC.presence_of_all_elements_located(self.PRICE_LOCATOR))
            count_before = len(elements)
            if not elements:
                break
            last = elements[-1]
            ActionChains(self.driver).scroll_to_element(last).perform()
            try:
                self.short_wait.until(
                    lambda d: len(d.find_elements(*self.PRICE_LOCATOR)) > count_before
                )
            except TimeoutException:
                break
