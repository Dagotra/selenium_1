from selenium.webdriver.common.by import By
from selenium_1.steam_site.base_page import BasePage


class SearchGamePage(BasePage):
    UNIQUE_ELEMENT_LOC = By.XPATH, "//body[contains(@class, 'search_page')]"
    SORT_SELECTOR = By.XPATH, "//div[@id='sort_by_dselect_container']"
    BUTTON_SEARCH_WITH_GAME_TEXT = By.XPATH, ("//div[@id='searchtag_tmpl' "
                                              "and not(contains(@style,'display: none'))]"
                                              "//span[contains(@class,'label')]")
    DROPLIST_SORT = By.XPATH, "//*[@id='sort_by_droplist']"
    DESC_PRICE_BUTTON = By.XPATH, f"{DROPLIST_SORT[1]}//a[@id='Price_DESC']"
    # SEARCH_RESULT_GAME = By.XPATH, "//*[@id='search_result_container']"
    PRICE_GAME = "(//div[contains(@class, 'search_discount_and_price')]//div[@data-price-final])[{}]"
    ATTRIBUTE_PRICE = "data-price-final"
    # LOADING_BAR = By.XPATH, "//*[@id='search_results_loading']"
    # CART_LOCATOR = By.XPATH, "//a[contains(@class,'search_result_row')]"
    PRICE_LOCATOR = By.XPATH, "//div[contains(@class,'discount_block') and @data-price-final]"
    DYNAMIC_LOC_NAME_GAME = "(//a[contains(@href, 'app')]//span[@class='title'])[{}]"

    def is_opened(self):
        """
        Проверка открытия страницы, наличием уникального локатора на странице
        """
        self.wait_visible(self.UNIQUE_ELEMENT_LOC)

    def check_open_page(self):
        """
        Проверка, что поиск именно данной игры.
        """
        text_game = self.get_text(self.BUTTON_SEARCH_WITH_GAME_TEXT).strip()
        if text_game.startswith('"') and text_game.endswith('"'):
            text_game = text_game[1:-1]
        return text_game

    def sort_descending_order(self):
        """
        Выставление сортировки по убыванию
        """
        self.wait_visible(self.SORT_SELECTOR)
        self.click(self.SORT_SELECTOR)
        self.wait_visible(self.DESC_PRICE_BUTTON)
        self.click(self.DESC_PRICE_BUTTON)

    def get_price_game(self, index):
        price = self.get_attribute(
            (By.XPATH, self.PRICE_GAME.format(index)),
            self.ATTRIBUTE_PRICE
        )
        return price

    def create_list_game(self, index):
        name_game = self.get_text((By.XPATH, self.DYNAMIC_LOC_NAME_GAME.format(index)))
        return name_game

    def refresh_locator(self):
        self.refresh(self.UNIQUE_ELEMENT_LOC)

    def check_decreasing_price(self):
        prices = []
        counter = len(self.wait_present_elements(self.PRICE_LOCATOR))
        for i in range(1, counter + 1):
            price = self.get_price_game(i)
            prices.append(int(price))
        assert prices == sorted(prices, reverse=True), "Баг разработки"
