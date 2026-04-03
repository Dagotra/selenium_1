from elements.input import Input
from logger.logger import Logger
from selenium.webdriver import Keys


class SliderElement(Input):

    def move_slider_to_right(self, move: int) -> None:
        self.js_focus()

        Logger.info(f"move slider '{move}' times")
        self._action_chains.send_keys(Keys.RIGHT * move).perform()

    def move_slider_to_left(self, move: int) -> None:
        self.js_focus()

        Logger.info(f"move slider '{move}' times")
        self._action_chains.send_keys(Keys.LEFT * move).perform()

    def set_value(self, value: float, step: float, target_value: float) -> float:
        Logger.info(f"{self}: {self.__class__.__name__}: set the slider value'")
        move = 1 / step
        differance = int(abs(target_value - value) * move)
        if value < target_value:
            self.move_slider_to_right(differance)
        elif value > target_value:
            self.move_slider_to_left(differance)

        return target_value
