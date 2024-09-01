class Vacancy:
    """Класс для представления вакансий"""

    def __init__(self, name, url, description, salary=0):
        self.name = name
        self.url = url
        self.description = description
        self.salary = salary