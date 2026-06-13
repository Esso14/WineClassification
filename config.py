import json
from logger import logger

class ConfigManager: 

    def __init__(self, config_path: str):
        self.config_path = config_path
        self._config = self._load()

    def _load(self) -> dict:
        with open(self.config_path, "r", encoding="utf-8") as file:
            config_data = json.load(file)
            logger.info(f"Configuration file is loaded")
            return config_data
        
    #--- Decorator: transforme methode in variable ----   
    @property
    def config(self):
        return self._config
        
    def get(self, key, default=None):
        return self._config.get(key, default)

