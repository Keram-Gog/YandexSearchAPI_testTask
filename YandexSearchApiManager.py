import requests
import xml.etree.ElementTree as ET
import SearchApiManager
import csv
import requests
import xml.etree.ElementTree as ET
import csv
from abc import ABC, abstractmethod

# Ваш основной класс для работы с Yandex API
class YandexSearchApiManager(SearchApiManager.SearchApiManager):
    """"класс, который наследуется от SearchApiManager и реализует конкретную логику работы с API Яндекса"""
    def search(self, query):
        """Метод для выполнения поискового запроса."""
        url = "https://yandex.ru/search/xml"
        params = {
            "apikey": self.api_key,
            "folderid": self.folder_id,
            "query": query,
            "lr": self.region,
            "l10n": "ru",
            "sortby": "rlv",
            "groupby": "attr=d.mode=deep.groups-on-page=10.docs-in-group=1",
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            return response.text
        else:
            print(f"Ошибка для запроса '{query}': {response.status_code}, {response.reason}")
            return None

    def parse_response(self, xml_response):
        """Метод для обработки ответа API."""
        root = ET.fromstring(xml_response)
        positions = {domain: {"top1": 0, "top3": 0, "top5": 0, "top10": 0} for domain in self.domains}
        results = []

        # Обработка первых 10 результатов
        for position, doc in enumerate(root.findall(".//doc"), start=1):
            if position > 10:
                break
            url = doc.find("url").text if doc.find("url") is not None else ""
            results.append((position, url))

            # Проверка доменов в URL
            for domain in self.domains:
                if domain in url:
                    if position == 1:
                        positions[domain]["top1"] += 1
                    if position <= 3:
                        positions[domain]["top3"] += 1
                    if position <= 5:
                        positions[domain]["top5"] += 1
                    if position <= 10:
                        positions[domain]["top10"] += 1

        return positions, results

    def save_to_csv(self, results, output_file):
        """Сохранение результатов в CSV файл."""
        with open(output_file, "w", encoding="utf-8", newline="") as f:
            # Определение заголовков для CSV
            fieldnames = ["query"] + \
                         [f"{domain}_top1" for domain in self.domains] + \
                         [f"{domain}_top3" for domain in self.domains] + \
                         [f"{domain}_top5" for domain in self.domains] + \
                         [f"{domain}_top10" for domain in self.domains]
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()

            # Запись данных о запросах
            for row in results:
                writer.writerow(row)

    def process_queries(self):
        """Метод для обработки запросов и сбора результатов."""
        results = []
        for query in self.queries:
            print(f"Обработка запроса: {query}")
            xml_response = self.search(query)
            if xml_response:
                positions, top_results = self.parse_response(xml_response)
                row = {
                    "query": query,
                }
                for domain in self.domains:
                    row.update({
                        f"{domain}_top1": positions[domain]["top1"],
                        f"{domain}_top3": positions[domain]["top3"],
                        f"{domain}_top5": positions[domain]["top5"],
                        f"{domain}_top10": positions[domain]["top10"],
                    })

                results.append(row)
        return results

    def display_results(self, results):
        """Вывод результатов в консоль."""
        for result in results:
            print(f"\nЗапрос: {result['query']}")
            for domain in self.domains:
                print(f"  {domain} - Top1: {result[f'{domain}_top1']} Top3: {result[f'{domain}_top3']} Top5: {result[f'{domain}_top5']} Top10: {result[f'{domain}_top10']}")

