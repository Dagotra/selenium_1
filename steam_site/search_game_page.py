from selenium.webdriver.common.by import By
from selenium_1.steam_site.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class SearchGamePage(BasePage):
    UNIQUE_ELEMENT_LOC = By.XPATH, "//body[contains(@class, 'search_page')]"
    SORT_SELECTOR = By.ID, "sort_by_dselect_container"
    DESC_PRICE_BUTTON = By.ID, "Price_DESC"
    PRICE_GAME = "(//div[contains(@class, 'search_discount_and_price')]//div[@data-price-final])[{}]"
    ATTRIBUTE_PRICE = "data-price-final"
    PRICE_LOCATOR = By.XPATH, "//div[contains(@class,'discount_block') and @data-price-final]"
    DYNAMIC_LOC_NAME_GAME = "(//a[contains(@href, 'app')]//span[@class='title'])[{}]"
    LOAD_BAR = By.ID, "search_results_loading"
    RESULT_ROW = By.XPATH, "//*[@id='search_resultsRows']/*"
    OPACITY_LOCATOR = By.XPATH, '//*[@id="search_result_container"] [contains(@style,"opacity")]'

    def waiting_for_page_to_open(self):
        """
        Проверка открытия страницы, наличием уникального локатора на странице
        """
        self.wait.until(EC.visibility_of_element_located(self.UNIQUE_ELEMENT_LOC))

    def sort_descending_order(self):
        """
        Выставление сортировки по убыванию
        """
        sort_selector = self.wait.until(EC.element_to_be_clickable(self.SORT_SELECTOR))
        sort_selector.click()
        price_button = self.wait.until(EC.visibility_of_element_located(self.DESC_PRICE_BUTTON))
        price_button.click()
        self.wait.until(EC.visibility_of_element_located(self.PRICE_LOCATOR))
        self.waiting_for_game_list_to_load()

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

    def get_prices(self):
        """Проверка сортировки в search_page списка всех игр по убыванию цены"""
        self.scroll_list_down()
        elements = self.wait.until(EC.presence_of_all_elements_located(self.PRICE_LOCATOR))
        prices = []
        for i in range(1, len(elements) + 1):
            raw = self.get_price_game(i)
            prices.append(int(raw) if raw and raw.isdigit() else 0)
        print(prices)
        return prices

    def scroll_list_down(self):
        """Метод скроллинга по списку отсортированных игр по убыванию до последней игры с ценой"""
        while True:
            elements = self.wait.until(EC.visibility_of_all_elements_located(self.PRICE_LOCATOR))
            count_before = len(elements)
            if not elements:
                break
            last = elements[-1]
            self.driver.execute_script("arguments[0].scrollIntoView();", last)
            try:
                self.wait.until(EC.visibility_of_element_located(self.LOAD_BAR))
                self.wait.until_not(EC.visibility_of_element_located(self.LOAD_BAR))
            finally:
                counter_after = len(self.wait.until(EC.visibility_of_all_elements_located(self.PRICE_LOCATOR)))
                print(counter_after, count_before)
                if counter_after <= count_before:
                    break

    def waiting_for_game_list_to_load(self):
        self.wait.until(EC.visibility_of_element_located(self.OPACITY_LOCATOR))
        self.wait.until_not(EC.visibility_of_element_located(self.OPACITY_LOCATOR))
