import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium_1.steam_site.home_page import HomePage


@pytest.fixture(scope="session")
def browser():
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

@pytest.fixture
def home_page(browser):
    page = HomePage(browser)
    page.open_page()
    return page
