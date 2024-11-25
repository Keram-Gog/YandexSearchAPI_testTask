import YandexSearchApiManager 
import DataManager
# Основной метод для запуска
def main():
    data_manager = DataManager.DataManager()
    data_manager.setup()

    search_api_manager = YandexSearchApiManager.YandexSearchApiManager(
        api_key=data_manager.config_manager.api_key,
        folder_id=data_manager.config_manager.catalog_id,
        queries=data_manager.queries,
        domains=data_manager.domains
    )

    output_file = input("Введите имя файла для сохранения результатов: ").strip()
    results = search_api_manager.process_queries()

    # Сохраняем результаты в файл
    search_api_manager.save_to_csv(results=results, output_file=output_file)

    # Выводим результаты в консоль
    search_api_manager.display_results(results=results)

    print(f"Результаты сохранены в {output_file}")

if __name__ == "__main__":
    """"главный скрипт, который связывает все классы и управляет процессом выполнения программы."""
    main()
