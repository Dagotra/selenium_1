import time
import platform

import pyautogui
import pyperclip

from logger.logger import Logger


class PyAutoGUIUtilities:
    @staticmethod
    def get_platform_system() -> str:
        Logger.debug(f"Проверяется операционная система на ПК")
        operation_system = platform.system()
        Logger.debug(f"Операционная система на ПК {operation_system}")
        return operation_system

    @staticmethod
    def upload_file(file_path: str) -> None:
        Logger.info("Обработка диалогового окна загрузки файла.")
        time.sleep(2)
        pyperclip.copy(file_path)
        Logger.info(f"'{file_path}' путь скопирован в буфер обмена.")
        system_name = PyAutoGUIUtilities.get_platform_system()
        time.sleep(1)
        Logger.info(f"ПРОВЕРЬ РАССКАЛДКУ, ДОЛЖНА БЫТЬ НА 'EN'")
        if system_name in ("Windows", "Linux"):
            pyautogui.hotkey("ctrl", "v")
            Logger.info(f"OC: {system_name}, применяем клавиши 'ctrl + v'")
        else:
            pyautogui.hotkey("Command", "v")
            Logger.info(f"OC: {system_name}, применяем клавиши 'Command + v'")
        time.sleep(1)
        Logger.info("Нажимаем 'Enter'")
        pyautogui.press("enter")
