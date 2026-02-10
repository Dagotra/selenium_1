from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

HOME_PAGE_URL = "https://store.steampowered.com/"
UNIQUE_ELEMENT_LOC = By.XPATH, '//*[@id="home_maincap_v7"]'
HEADER_LOC = By.XPATH, '//div[@role="navigation"]'
SEARCH_INPUT = By.XPATH, f'{HEADER_LOC[1]}//form[@role="search"]'
SEARCH_BUTTON = By.XPATH, f'{HEADER_LOC[1]}//button[@type="submit"]'
TIMEOUT_WEB_DRIVER = 10

wait = WebDriverWait
driver = webdriver.Chrome
def search_unique_page_element():
    """Поиск уникального элемента на главной странице"""
    element = 2