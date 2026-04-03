import random
from logger.logger import Logger


class RandomUtils:
    @staticmethod
    def get_random_value_in_range(min_value: float, max_value: float, step_value: float) -> float:
        Logger.info(f"{__class__.__name__}: get random value in range between '{min_value}' and '{max_value}'")
        target_value = random.randint(int(min_value / step_value + 1), int(max_value / step_value - 1)) * step_value
        decimal = len(str(step_value).split(".")[-1]) if "." in str(step_value) else 0

        Logger.info(f"target value: '{target_value}'")
        return round(target_value, decimal)
