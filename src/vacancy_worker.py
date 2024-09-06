from abc import ABC, abstractmethod


class VacancyWorker(ABC):
    """Абстрактный класс для работы с вакансиями"""

    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def get_vacancy_by_criterion(self, word):
        pass

    @abstractmethod
    def del_vacancy(self, vacancy):
        pass


class VacancyWorkerHH(VacancyWorker):
    """Класс для сохранения информации о вакансиях в json-файл"""

    def __init__(self, vacancies: list[dict]):
        self.vacancies = vacancies

    def add_vacancy(self, vacancy: dict):
        """Добавляет вакансию"""
        if vacancy.get("name").lower() not in [vac.get("name").lower() for vac in self.vacancies]:
            self.vacancies.append(vacancy)

    def get_vacancy_by_criterion(self, word: str):
        """Получает вакансии по критерию"""
        searched_vacancies = [vac for vac in self.vacancies if
                              word in vac["name"].lower or word in vac["description"].lower()]

        return searched_vacancies

    def del_vacancy(self, vacancy: dict):
        """Удаляет вакансию"""
        for index, vac in enumerate(self.vacancies):
            if vac["name"].lower() == vacancy["name"].lower():
                self.vacancies.pop(index)
