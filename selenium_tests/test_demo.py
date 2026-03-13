import time

from logger.logger import Logger
from browser.browser import Browser
from pages.horizontal_slider_page import HorizontalSliderPage
from pages.start_page import StartPage
from pages.alert_page import AlertPage
from pages.context_menu_page import ContextMenuPage
from pages.hovers_page import HoversPage
from pages.interactions_page import InteractionsPage
from pages.new_window_page import NewWindowPage
from faker import Faker

fake = Faker()


def test_basic_authorization(driver):
    url_basic_authorization = "http://admin:admin@the-internet.herokuapp.com/basic_auth"
    Logger.info(f"Запускаем тест '{test_basic_authorization.__name__}'")

    br = Browser(driver)
    sp = StartPage(br)
    expected_text = 'Congratulations! You must have the proper credentials.'

    br.get(url_basic_authorization)
    sp.wait_for_open()
    actual_text = sp.get_success_message()
    assert actual_text == expected_text, (
        f"Ожидаемый результат: '{expected_text}'. Фактический результат: '{actual_text}'."
    )


def test_alerts(driver):
    url_alerts = "https://the-internet.herokuapp.com/javascript_alerts"
    Logger.info(f"Запускаем тест '{test_alerts.__name__}'")

    br = Browser(driver)
    ap = AlertPage(br)
    text_in_alert = fake.text()
    expected_js_alert_text = 'I am a JS Alert'
    expected_js_confirm_text = 'I am a JS Confirm'
    expected_js_prompt_text = 'I am a JS prompt'
    expected_result_alert_text = 'You successfully clicked an alert'
    expected_result_confirm_text = 'You clicked: Ok'
    expected_result_prompt_text = 'You entered: ' + f"{text_in_alert}"

    br.get(url_alerts)
    ap.wait_for_open()
    actual_js_alert_text = ap.get_js_alert_text()
    assert actual_js_alert_text == expected_js_alert_text, (
        f"Ожидаемый результат: '{expected_js_alert_text}'. "
        f"Фактический результат: '{actual_js_alert_text}'."
    )

    br.close_alert()
    actual_js_alert_result_text = ap.get_text_result()
    assert actual_js_alert_result_text == expected_result_alert_text, (
        f"Ожидаемый результат: '{expected_result_alert_text}'. "
        f"Фактический результат: '{actual_js_alert_result_text}'."
    )

    actual_js_confirm_text = ap.get_js_confirm_text()
    assert actual_js_confirm_text == expected_js_confirm_text, (
        f"Ожидаемый результат: '{expected_js_confirm_text}'. "
        f"Фактический результат: '{actual_js_confirm_text}'."
    )

    br.close_alert()
    actual_js_confirm_result_text = ap.get_text_result()
    assert actual_js_confirm_result_text == expected_result_confirm_text, (
        f"Ожидаемый результат: '{expected_result_confirm_text}'. "
        f"Фактический результат: '{actual_js_confirm_result_text}'."
    )

    actual_js_prompt_text = ap.get_js_prompt_text()
    br.send_keys_in_alert(text_in_alert)
    br.close_alert()
    assert actual_js_prompt_text == expected_js_prompt_text, (
        f"Ожидаемый результат: '{expected_js_prompt_text}'. "
        f"Фактический результат: '{actual_js_prompt_text}'."
    )

    actual_js_prompt_result_text = ap.get_text_result()
    assert actual_js_prompt_result_text == " ".join(expected_result_prompt_text.split()), (
        f"Ожидаемый результат: '{expected_result_prompt_text}'. "
        f"Фактический результат: '{actual_js_prompt_result_text}'."
    )


def test_alerts_plus_js(driver):
    url_alerts_plus_js = "https://the-internet.herokuapp.com/javascript_alerts"
    Logger.info(f"Запускаем тест '{test_alerts_plus_js.__name__}'")

    br = Browser(driver)
    ap = AlertPage(br)
    text_in_alert = fake.text()
    expected_js_alert_text = 'I am a JS Alert'
    expected_js_confirm_text = 'I am a JS Confirm'
    expected_js_prompt_text = 'I am a JS prompt'
    expected_result_alert_text = 'You successfully clicked an alert'
    expected_result_confirm_text = 'You clicked: Ok'
    expected_result_prompt_text = 'You entered: ' + f"{text_in_alert}"

    br.get(url_alerts_plus_js)
    ap.wait_for_open()
    actual_js_alert_text = ap.get_js_method_alert_text()
    assert actual_js_alert_text == expected_js_alert_text, (
        f"Ожидаемый результат: '{expected_js_alert_text}'. "
        f"Фактический результат: '{actual_js_alert_text}'."
    )

    br.close_alert()
    actual_js_alert_result_text = ap.get_text_result()
    assert actual_js_alert_result_text == expected_result_alert_text, (
        f"Ожидаемый результат: '{expected_result_alert_text}'. "
        f"Фактический результат: '{actual_js_alert_result_text}'."
    )

    actual_js_confirm_text = ap.get_js_method_confirm_text()
    assert actual_js_confirm_text == expected_js_confirm_text, (
        f"Ожидаемый результат: '{expected_js_confirm_text}'. "
        f"Фактический результат: '{actual_js_confirm_text}'."
    )

    br.close_alert()
    actual_js_confirm_result_text = ap.get_text_result()
    assert actual_js_confirm_result_text == expected_result_confirm_text, (
        f"Ожидаемый результат: '{expected_result_confirm_text}'. "
        f"Фактический результат: '{actual_js_confirm_result_text}'."
    )

    actual_js_prompt_text = ap.get_js_method_prompt_text()
    br.send_keys_in_alert(text_in_alert)
    br.close_alert()
    assert actual_js_prompt_text == expected_js_prompt_text, (
        f"Ожидаемый результат: '{expected_js_prompt_text}'. "
        f"Фактический результат: '{actual_js_prompt_text}'."
    )

    actual_js_prompt_result_text = ap.get_text_result()
    assert actual_js_prompt_result_text == " ".join(expected_result_prompt_text.split()), (
        f"Ожидаемый результат: '{expected_result_prompt_text}'. "
        f"Фактический результат: '{actual_js_prompt_result_text}'."
    )


def test_alerts_plus_context_click(driver):
    url_alerts_plus_context_click = "http://the-internet.herokuapp.com/context_menu"
    Logger.info(f"Запускаем тест '{test_alerts_plus_context_click.__name__}'")
    expected_alert_text = "You selected a context menu"

    br = Browser(driver)
    cm = ContextMenuPage(br)

    br.get(url_alerts_plus_context_click)
    cm.wait_for_open()
    actual_alert_text = cm.get_text_alert()
    assert actual_alert_text == expected_alert_text, (
        f"Ожидаемый результат: '{expected_alert_text}'. "
        f"Фактический результат: '{actual_alert_text}'."
    )
    br.close_alert()


def test_action(driver):
    url_actions = "http://the-internet.herokuapp.com/horizontal_slider"
    Logger.info(f"Запускаем тест '{test_action.__name__}'")

    br = Browser(driver)
    hs = HorizontalSliderPage(br)

    br.get(url_actions)
    hs.wait_for_open()
    expected_number = hs.set_random_slider_value()
    actual_number = hs.get_slider_value_text()
    assert actual_number == expected_number, (
        f"Ожидаемый результат: '{expected_number}'. "
        f"Фактический результат: '{actual_number}'."
    )


def test_hover(driver):
    url_hover = "http://the-internet.herokuapp.com/hovers"
    Logger.info(f"Запускаем тест '{test_hover.__name__}'")
    index_user = [1, 2, 3]

    br = Browser(driver)
    hrs = HoversPage(br)

    br.get(url_hover)
    hrs.wait_for_open()
    for _, value in enumerate(index_user):
        expected_url_user = f"https://the-internet.herokuapp.com/users/{value}"
        expected_text_user = f'name: user{value}'
        hrs.hover_user(value)
        actual_text_user = hrs.get_text_in_hover_user(value)
        assert actual_text_user == expected_text_user, (
            f"Ожидаемый результат: '{expected_text_user}'. "
            f"Фактический результат: '{actual_text_user}'."
        )
        hrs.click_view_profile_user(value)
        actual_url_user = br.get_current_url()
        assert actual_url_user == expected_url_user, (
            f"Ожидаемый результат: '{expected_url_user}'. "
            f"Фактический результат: '{actual_url_user}'."
        )
        br.go_back_to_previous_page()


def test_handlers(driver):
    url_interactions = "http://the-internet.herokuapp.com/windows"
    excepted_text_in_new_tab = "New Window"
    excepted_name_new_title = "New Window"
    Logger.info(f"Запускаем тест '{test_handlers.__name__}'")

    br = Browser(driver)
    isp = InteractionsPage(br)
    nwp = NewWindowPage(br)

    br.get(url_interactions)
    isp.wait_for_open()
    isp.click_button_click_here()

    br.switch_to_last_tab()
    nwp.wait_for_open()

    actual_name_new_title = br.get_name_title()
    assert actual_name_new_title == excepted_name_new_title, (
        f"Ожидаемый результат: '{excepted_name_new_title}'. "
        f"Фактический результат: '{actual_name_new_title}'."
    )
    actual_text_in_new_tab = nwp.get_text_new_tab()
    assert actual_text_in_new_tab == excepted_text_in_new_tab, (
        f"Ожидаемый результат: '{excepted_text_in_new_tab}'. "
        f"Фактический результат: '{actual_text_in_new_tab}'."
    )

    br.switch_to_first_tab()
    isp.wait_for_open()
    isp.click_button_click_here()

    br.switch_to_any_tab(2)
    assert actual_name_new_title == excepted_name_new_title, (
        f"Ожидаемый результат: '{excepted_name_new_title}'. "
        f"Фактический результат: '{actual_name_new_title}'."
    )
    actual_text_in_new_tab = nwp.get_text_new_tab()
    assert actual_text_in_new_tab == excepted_text_in_new_tab, (
        f"Ожидаемый результат: '{excepted_text_in_new_tab}'. "
        f"Фактический результат: '{actual_text_in_new_tab}'."
    )

    br.switch_to_first_tab()
    isp.wait_for_open()
    br.switch_to_last_tab()
    br.close_tab()
    br.switch_to_last_tab()
    br.close_tab()
