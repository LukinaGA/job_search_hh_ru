import requests

from abc import ABC, abstractmethod


class Parser(ABC):

    @abstractmethod
    def __api_connect(self):
        """Подключение к API"""
        pass

    @abstractmethod
    def load_vacancies(self, keyword):
        """Получает вакансии по ключевому слову"""
        pass


class HeadHunterAPI(Parser):
    """Класс для работы с API HeadHunter"""

    def __init__(self):
        self.__url = 'https://api.hh.ru/vacancies'
        self.__headers = {'User-Agent': 'HH-User-Agent'}
        self.__params = {'text': '', 'page': 0, 'per_page': 100}
        self.vacancies = []

    def _Parser__api_connect(self):
        """Подключение к API hh.ru"""
        response = requests.get(self.__url, headers=self.__headers, params=self.__params)
        if response.status_code == 200:
            return response

        print("Ошибка получения данных")

    def load_vacancies(self, keyword: str) -> list:
        """Получение вакансий по ключевому слову"""
        self.__params['text'] = keyword
        while self.__params.get('page') != 20:
            response = self._Parser__api_connect()
            if response:
                vacancies = response.json()['items']
                self.vacancies.extend(vacancies)
                self.__params['page'] += 1
            else:
                self.vacancies = []
                break

        return self.vacancies
