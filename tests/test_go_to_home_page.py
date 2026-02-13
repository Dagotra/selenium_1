import pytest
from selenium_1.config.config_reader import ConfigReader
from selenium_1.steam_site.home_page import HomePage
from selenium_1.steam_site.search_game_page import SearchGamePage

N = [10, 20]
MIN_RANGE = 1
MAX_RANGE_WITCHER = N[0] + 1
MAX_RANGE_FALLOUT = N[1] + 1

@pytest.mark.xfail(reason="Нарушенная сортировка по убыванию цены")
@pytest.mark.parametrize("game,lang", [
    ("The Witcher", "russian"),
    ("The Witcher", "english"),
    ("Fallout", "russian"),
    ("Fallout", "english"),
])
def test_search_game(browser, game, lang):
    """Тест поиска игры с разными языками"""
    config = ConfigReader()
    url = config.get("app", "base_url")
    browser.get(url)
    home = HomePage()
    search = SearchGamePage()
    home.wait_unique_element()
    current_lang = home.check_language()
    if lang == "russian":
        if current_lang != "ru":
            home.change_language(config.get("app", "default_language"))
    else:
        if current_lang == "ru":
            home.change_language(config.get("app", "english"))
    max_range = MAX_RANGE_WITCHER if game == "The Witcher" else MAX_RANGE_FALLOUT
    home.enter_game_name(game)
    home.click_search()
    search.open_page()
    search.check_open_page()
    search.sort_descending_order()
    search.refresh_locator()
    list_games = [search.create_list_game(i) for i in range(MIN_RANGE, max_range)]
    # print(list_games) Список игр отфильтрованных по убыванию цен
    prices = search.get_prices()
    assert prices == sorted(prices, reverse=True), "Баг разработки!!!"