import time
import platform
import os

import pyperclip

from logger.logger import Logger


class PyAutoGUIUtilities:
    @staticmethod
    def _get_pyautogui():
        if platform.system() == "Linux" and not os.environ.get("DISPLAY"):
            raise RuntimeError("PyAutoGUI недоступен без DISPLAY. ")
        import pyautogui
        return pyautogui

    @staticmethod
    def upload_file(file_path: str) -> None:
        pyautogui = PyAutoGUIUtilities._get_pyautogui()
        Logger.info("Обработка диалогового окна загрузки файла.")
        time.sleep(2)
        pyperclip.copy(file_path)
        Logger.info(f"'{file_path}' путь скопирован в буфер обмена.")

        Logger.debug(f"Проверяется операционная система на ПК")
        system_name = platform.system()
        Logger.debug(f"Операционная система на ПК {system_name}")

        time.sleep(1)
        if system_name in ("Windows", "Linux"):
            pyautogui.hotkey("ctrl", "v")
            Logger.info(f"OC: {system_name}, применяем клавиши 'ctrl + v'")
        else:
            pyautogui.hotkey("Command", "v")
            Logger.info(f"OC: {system_name}, применяем клавиши 'Command + v'")
        time.sleep(1)
        Logger.info("Нажимаем 'Enter'")
        pyautogui.press("enter")
