from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from faker import Faker

fake = Faker()
URL = "https://store.steampowered.com/"
UNIQ_ELEMENT_MAIN_PAGE = By.XPATH, '//*[@id="home_maincap_v7"]'
ENTRANCE_BUTTON = By.XPATH, "//*[@id='global_actions']//a[contains(@href, 'login')]"
OBJECT_LOGIN = By.XPATH, "//div[@data-featuretarget='login']"
INPUT_LOGIN = By.XPATH, f"{OBJECT_LOGIN[1]}//input[@type='text']"
INPUT_PASSWORD = By.XPATH, f"{OBJECT_LOGIN[1]}//input[@type='password']"
LOGIN_BUTTON = By.XPATH, f"{OBJECT_LOGIN[1]}//button[@type='submit']"
LOADER = By.XPATH, f"{OBJECT_LOGIN[1]}//button[@type='submit']//div//div"
ERROR_TEXT = By.XPATH, f"({OBJECT_LOGIN[1]}//div)[20]"
STRING_ERROR_TEXT = "Пожалуйста, проверьте свой пароль и имя аккаунта и попробуйте снова."
TIMEOUT_WEBDRIVER = 10


def test_error_login_steam(browser):
    wait = WebDriverWait(browser, TIMEOUT_WEBDRIVER)

    browser.get(URL)

    wait.until(
        EC.visibility_of_element_located(UNIQ_ELEMENT_MAIN_PAGE),
        message=(
            f"Уникальный элемент страницы '{UNIQ_ELEMENT_MAIN_PAGE[1]}' "
            f"не найден за '{TIMEOUT_WEBDRIVER}' секунд."
        )
    )

    wait.until(EC.element_to_be_clickable(ENTRANCE_BUTTON)).click()
    wait.until(EC.visibility_of_element_located(OBJECT_LOGIN))

    wait.until(EC.visibility_of_element_located(INPUT_LOGIN)).send_keys(fake.email())
    wait.until(EC.visibility_of_element_located(INPUT_PASSWORD)).send_keys(fake.password())

    wait.until(EC.visibility_of_element_located(LOGIN_BUTTON)).click()

    wait.until(EC.presence_of_element_located(LOADER))

    wait.until(EC.invisibility_of_element_located(LOADER))

    error_text = wait.until(EC.visibility_of_element_located(ERROR_TEXT))
    text = error_text.text
    assert STRING_ERROR_TEXT == text, \
        (f"Неверный текст ошибки. Ожидаемый результат: '{text}'."
         f"Фактический результат: '{STRING_ERROR_TEXT}'")
