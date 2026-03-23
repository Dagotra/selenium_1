import os
import tempfile
import time

import pytest
from browser.browser_factory import BrowserFactory
from logger.logger import Logger


@pytest.fixture(scope="session")
def driver():
    print()
    Logger.info(f"Создаем фикстуру")
    driver = BrowserFactory.get_driver()
    yield driver
    print()
    Logger.info(f"Закрываем вэбдрайвер '{driver.name}' ")
    driver.quit()
    Logger.info("Сессия закрыта")


@pytest.fixture
def upload_test_file_path(tmp_path) -> str: # Создание и удаление файла в папке Pytest-а tmp_path
    file_name = "text_file.txt"
    file_path = tmp_path / file_name
    Logger.info(f"Создаем временный файл: '{file_name}' и путь к нему '{file_path}' ")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write("test file")
    Logger.info(f"Файл {file_name} создан")
    return str(file_path)


@pytest.fixture(scope="function")
def upload_test_file_path_remove(): # Классическое создание и удаление временного файла в temp
    with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".txt", encoding="utf-8") as f:
        path_to_file = f.name
        file_name = os.path.basename(path_to_file)
        Logger.info(f"Создаем временный файл: '{file_name}' и путь к нему '{path_to_file}'")
        f.write("test file")
    yield path_to_file
    try:
        Logger.info(f"Удаляем файл '{file_name}', путь к файлу '{path_to_file}'")
        os.remove(path_to_file)
    except PermissionError as err:
        Logger.error(f"Ошибка: {err}, вторая попытка удаления файла '{file_name}'")
        time.sleep(2)
        os.remove(path_to_file)


