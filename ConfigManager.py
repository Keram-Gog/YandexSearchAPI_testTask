class ConfigManager:
  """"класс, который управляет конфигурационными данными (ключ API и идентификатор каталога)."""
  def __init__(self):
      self.catalog_id = None
      self.api_key = None
      
  def set_catalog_data(self):
      """Запрашивает и сохраняет идентификатор каталога и ключ API.
        catalog_id: Идентификатор каталога.
        api_key: Ключ API, выданный сервисом.
        """
      self.catalog_id = input("Введите идентификатор каталога: ").strip()
      self.api_key = input("Введите ключ API: ").strip()