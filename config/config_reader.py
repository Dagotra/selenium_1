from typing import Any
import yaml


class ConfigReader:
    def __init__(self, path: str = "config/config.yaml"):
        self.path = path
        self.data = self._load()

    def _load(self) -> dict[str, Any]:
        with open(self.path, "r", encoding='utf-8') as f:
            file = yaml.safe_load(f)
        return file

    def get(self, key, nested_key=None):
        selection = self.data.get(key)
        if selection is None:
            return None
        if nested_key is not None and isinstance(selection, dict):
            return selection.get(nested_key)
        return selection
