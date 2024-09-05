import json
import os.path
from abc import ABC, abstractmethod

from config import DATA_DIR


class Saver(ABC):

    @abstractmethod
    def save_to_file(self, vacancies):
        pass


class JSONSaver(Saver):

    def __init__(self, file="vacancies.json"):
        self.__file = os.path.join(DATA_DIR, file)

    def save_to_file(self, vacancies: list) -> None:
        """Сохраняет данные в json-файл"""
        with open(self.__file, "a", encoding="utf-8") as f:
            json.dump(vacancies, f, ensure_ascii=False)