class InputManager:
    """"класс для ввода данных пользователем (запросов и доменов)."""
    def read_from_file(self, input_file):
        """Чтение данных из файла и сохранение в список.
        Args: input_file (str): Путь к файлу.
        Returns: list: Список строк из файла.
        """
        with open(input_file, "r", encoding="utf-8") as f:
            return [line.strip() for line in f.readlines()]

    def get_input_from_console(self, prompt):
        """Циклично запрашивает ввод с консоли и сохраняет в список."""
        data = []
        print(f"{prompt} (для завершения ввода введите 'exit'):")
        while True:
            user_input = input("Введите данные: ")
            if user_input.lower() == 'exit':
                break
            data.append(user_input)
        return data

    def set_queries(self):
        """Запрашивает и сохраняет запросы (из файла или с консоли)."""
        method = input("Как удобно: сохранить запросы в файл (введите 'file') или вводить с консоли (введите 'console')? ").strip().lower()
        if method == 'file':
            input_file = input("Введите путь к файлу для чтения запросов: ").strip()
            return self.read_from_file(input_file)
        elif method == 'console':
            return self.get_input_from_console("Введите запросы")
        else:
            print("Некорректный ввод. Пожалуйста, выберите 'file' или 'console'.")
