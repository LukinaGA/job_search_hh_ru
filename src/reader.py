import json
import os.path
from abc import ABC, abstractmethod

from config import DATA_DIR


class Reader(ABC):

    @abstractmethod
    def read_file(self):
        pass


class JSONReader(Reader):

    def __init__(self, file="vacancies.json"):
        self.__file = os.path.join(DATA_DIR, file)

    def read_file(self) -> list[dict]:
        """Считывает данные из json-файла"""
        with open(self.__file, encoding="utf-8") as f:
            data = json.load(f)

        return data
