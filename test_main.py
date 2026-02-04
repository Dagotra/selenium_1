from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from faker import Faker

fake = Faker()
URL = "https://store.steampowered.com/"
ENTRANCE_BUTTON = "//*[@id='global_actions']//a[contains(@href, 'login')]"
OBJECT_LOGIN = "//div[@data-featuretarget='login']"
INPUT_LOGIN = OBJECT_LOGIN + "//input[@type='text']"
INPUT_PASSWORD = OBJECT_LOGIN + "//input[@type='password']"
LOGIN_BUTTON = OBJECT_LOGIN + "//button[@type='submit']"
LOADER = LOGIN_BUTTON + "//div//div"
ERROR_TEXT = "//div[@data-featuretarget='login']//div[contains(text(), 'проверьте свой пароль')]"


def test_error_login_steam():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    try:
        driver.get(URL)
        assert URL in driver.current_url, "Это не главная страница"

        wait.until(EC.element_to_be_clickable((By.XPATH, ENTRANCE_BUTTON))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, OBJECT_LOGIN)))

        wait.until(EC.visibility_of_element_located((By.XPATH, INPUT_LOGIN))).send_keys(fake.email())
        driver.find_element(By.XPATH, INPUT_PASSWORD).send_keys(fake.password())

        driver.find_element(By.XPATH, LOGIN_BUTTON).click()

        wait.until(EC.presence_of_element_located((By.XPATH, LOADER)))
        wait.until(EC.invisibility_of_element_located((By.XPATH, LOADER)))

        wait.until(EC.visibility_of_element_located((By.XPATH, ERROR_TEXT)))

    finally:
        driver.quit()
