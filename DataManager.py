import ConfigManager
import InputManager

class DataManager:
    """"класс, который управляет данными: запрашивает ключ API, идентификатор каталога, запросы и домены"""
    def __init__(self):
        self.config_manager = ConfigManager.ConfigManager()
        self.input_manager = InputManager.InputManager()

    def setup(self):
        """Запрашивает все необходимые данные для работы."""
        self.config_manager.set_catalog_data()
        self.queries = self.input_manager.set_queries()
        self.domains = self.input_manager.set_queries()

    def display_data(self):
        """Выводит все собранные данные."""
        print(f"Идентификатор каталога: {self.config_manager.catalog_id}")
        print(f"Ключ API: {self.config_manager.api_key}")
        print(f"Запросы: {self.queries}")
        print(f"Доменов: {self.domains}")