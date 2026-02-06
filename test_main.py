from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from faker import Faker

fake = Faker()
URL = "https://store.steampowered.com/"
ENTRANCE_BUTTON = By.XPATH, "//*[@id='global_actions']//a[contains(@href, 'login')]"
OBJECT_LOGIN = By.XPATH, "//div[@data-featuretarget='login']"
INPUT_LOGIN = By.XPATH, "//div[@data-featuretarget='login']//input[@type='text']"
INPUT_PASSWORD = By.XPATH, "//div[@data-featuretarget='login']//input[@type='password']"
LOGIN_BUTTON = By.XPATH, "//div[@data-featuretarget='login']//button[@type='submit']"
LOADER = By.XPATH, "//div[@data-featuretarget='login']//button[@type='submit']//div//div"
ERROR_TEXT = By.XPATH, "(//div[@data-featuretarget='login']//div)[20]"
STRING_ERROR_TEXT = "Пожалуйста, проверьте свой пароль и имя аккаунта и попробуйте снова."


def test_error_login_steam(browser):
    wait = WebDriverWait(browser, 10)

    browser.get(URL)
    assert URL in browser.current_url, "Это не главная страница"

    wait.until(EC.element_to_be_clickable(ENTRANCE_BUTTON)).click()
    wait.until(EC.visibility_of_element_located(OBJECT_LOGIN))

    wait.until(EC.visibility_of_element_located(INPUT_LOGIN)).send_keys(fake.email())
    wait.until(EC.visibility_of_element_located(INPUT_PASSWORD)).send_keys(fake.password())

    wait.until(EC.visibility_of_element_located(LOGIN_BUTTON)).click()

    wait.until(EC.presence_of_element_located(LOADER))

    wait.until(EC.invisibility_of_element_located(LOADER))

    wait.until(EC.visibility_of_element_located(ERROR_TEXT))
    text = wait.until(EC.visibility_of_element_located(ERROR_TEXT)).text
    assert STRING_ERROR_TEXT == text, \
        f"Текст ошибки при невалидной авторизации не совпадает с шаблоном текста '{STRING_ERROR_TEXT}'"
