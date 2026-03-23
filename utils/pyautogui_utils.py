import time
import platform

import pyautogui
import pyperclip

from logger.logger import Logger


class PyAutoGUIUtilities:
    @staticmethod
    def get_platform_system() -> bool:
        Logger.debug(f"Проверяется операционная система на ПК")
        operation_system = platform.system()
        Logger.debug(f"Операционная система на ПК {operation_system}")
        if operation_system == "Window" or "Linux":
            return True
        return False

    @staticmethod
    def upload_file(file_path: str) -> None:
        Logger.info("Обработка диалогового окна загрузки файла.")
        time.sleep(1)
        pyperclip.copy(file_path)
        if PyAutoGUIUtilities.get_platform_system():
            pyautogui.hotkey("ctrl", "v")
        else:
            pyautogui.hotkey("Command", "v")
        Logger.info(f"'{file_path}' копируется в поле поиска диалогового окна.")
        Logger.info("Нажимаем 'Enter'")
        pyautogui.hotkey("enter")
        time.sleep(1)
