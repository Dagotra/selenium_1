import pytest
from selenium_1.steam_site.home_page import HomePage
from selenium_1.steam_site.search_game_page import SearchGamePage

LIST_TESTING_GAME = ["The Witcher", "Fallout"]
LIST_LANGUAGE = ["russian", "english"]
MIN_RANGE = 1
MAX_RANGE_WITCHER = 11
MAX_RANGE_FALLOUT = 21


@pytest.mark.xfail(reason="Сортировка багована")
def test_search_game_witcher_ru(browser):
    """Тест ввода игры The Witcher в поисковик на русском языке"""
    prices = []
    home = HomePage(browser)
    search = SearchGamePage(browser)
    home.open_page()
    home.wait_unique_element()
    home.check_language(LIST_LANGUAGE[0])
    home.enter_game_name(LIST_TESTING_GAME[0])
    home.click_search()
    search.is_opened()
    search.check_open_page()
    search.sort_descending_order()
    search.refresh_locator()
    for i in range(MIN_RANGE, MAX_RANGE_WITCHER):
        name = search.create_list_game(i)
        prices.append(name)

    print(prices)


def test_search_game_witcher_eng(browser):
    """Тест ввода игры The Witcher в поисковик на английском языке"""
    prices = []
    home = HomePage(browser)
    search = SearchGamePage(browser)
    home.open_page()
    home.wait_unique_element()
    home.check_language(LIST_LANGUAGE[1])
    home.enter_game_name(LIST_TESTING_GAME[0])
    home.click_search()
    search.is_opened()
    search.check_open_page()
    search.sort_descending_order()
    search.refresh_locator()
    for i in range(MIN_RANGE, MAX_RANGE_WITCHER):
        name = search.create_list_game(i)
        prices.append(name)

    print(prices)


def test_checking_move_fallout_ru(browser):
    """Тест ввода игры Fallout в поисковик на русском языке"""
    prices = []
    home = HomePage(browser)
    search = SearchGamePage(browser)
    home.open_page()
    home.wait_unique_element()
    home.check_language(LIST_LANGUAGE[0])
    home.enter_game_name(LIST_TESTING_GAME[1])
    home.click_search()
    search.is_opened()
    search.check_open_page()
    search.sort_descending_order()
    search.refresh_locator()
    for i in range(MIN_RANGE, MAX_RANGE_FALLOUT):
        name = search.create_list_game(i)
        prices.append(name)

    print(prices)


def test_checking_move_search_fallout_eng(browser):
    """Тест ввода игры Fallout в поисковик на английском языке"""
    prices = []
    home = HomePage(browser)
    search = SearchGamePage(browser)
    home.open_page()
    home.wait_unique_element()
    home.check_language(LIST_LANGUAGE[0])
    home.enter_game_name(LIST_TESTING_GAME[1])
    home.click_search()
    search.is_opened()
    search.check_open_page()
    search.sort_descending_order()
    search.refresh_locator()
    for i in range(MIN_RANGE, MAX_RANGE_FALLOUT):
        name = search.create_list_game(i)
        prices.append(name)

    print(prices)
