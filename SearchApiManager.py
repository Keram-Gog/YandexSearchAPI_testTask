from abc import ABC, abstractmethod
import requests
import xml.etree.ElementTree as ET


class SearchApiManager(ABC):
    """"базовый класс для работы с API. Он определяет общие методы для выполнения запросов и обработки ответов"""
    def __init__(self, api_key, folder_id, queries, domains, region="213"):
        self.api_key = api_key
        self.folder_id = folder_id
        self.queries = queries
        self.domains = domains
        self.region = region

    @abstractmethod
    def search(self, query):
        """Метод для выполнения поискового запроса."""
        pass

    @abstractmethod
    def parse_response(self, response):
        """Метод для обработки ответа API."""
        pass

    def process_queries(self):
        results = []
        for query in self.queries:
            print(f"Обработка запроса: {query}")
            response = self.search(query)
            if response:
                parsed_data = self.parse_response(response)
                results.append(parsed_data)
        return results
