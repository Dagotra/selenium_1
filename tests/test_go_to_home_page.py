import pytest
from selenium_1.config.config_reader import ConfigReader
from selenium_1.steam_site.home_page import HomePage
from selenium_1.steam_site.search_game_page import SearchGamePage

N = [10, 20]
MIN_RANGE = 1
GAME_1 = "The Witcher"
GAME_2 = "Fallout"


# @pytest.mark.xfail(reason="Нарушенная сортировка по убыванию цены")
# Баг сортировки, такой бы флаг повесил в разработке Steam
@pytest.mark.parametrize("game, max_range", [(GAME_1, N[0]), (GAME_2, N[1])])
@pytest.mark.parametrize("browser", ["ru", "en"], indirect=True)
def test_search_game(browser, game, max_range):
    """Тест поиска игры с разными языками"""
    config = ConfigReader()
    home = HomePage()
    search = SearchGamePage()

    url = config.get("app", "base_url")
    browser.get(url)
    home.wait_unique_element()
    home.enter_game_name(game)
    home.click_search()
    search.waiting_for_page_to_open()
    search.sort_descending_order()
    browser.refresh()
    list_games = [search.create_list_game(i) for i in range(MIN_RANGE, max_range + 1)]
    # print(list_games)  # Список игр отфильтрованных по убыванию цен
    # print(len(list_games))  # Список игр отфильтрованных по убыванию цен
    prices = search.get_prices()
    assert prices == sorted(prices, reverse=True), (f"Сортировка списка по ценам невалидная. "
                                                    f"Актуальный порядок сортировки цен: "
                                                    f"{sorted(prices, reverse=True)}\n"
                                                    f"Фактический {prices} ")
