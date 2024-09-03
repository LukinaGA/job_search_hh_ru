class Vacancy:
    """Класс для представления вакансий"""
    __slots__ = ("name", "url", "description", "salary")

    def __init__(self, name: str, url: str, description: str, salary=None):
        self.name = name
        self.url = url
        self.description = description
        self.salary = self.__salary_validation(salary)

    @staticmethod
    def __salary_validation(salary):
        if salary:
            return salary
        return 0

    @classmethod
    def new_vacancy(cls, vacancy_dict: dict) -> "Vacancy":
        """Создаёт новый экземпляр класса Vacancy из словаря"""
        name = vacancy_dict.get("name")
        url = vacancy_dict.get("alternate_url")
        description = vacancy_dict.get('snippet').get('responsibility')
        if vacancy_dict.get("salary"):
            if vacancy_dict.get("salary").get("to"):
                salary = vacancy_dict.get("salary").get("to")
            elif vacancy_dict.get("salary").get("from"):
                salary = vacancy_dict.get("salary").get("from")
        else:
            salary = 0

        return cls(name, url, description, salary)

    def __str__(self):
        return f"{self.name} (ЗП {self.salary} руб). {self.description}. Ссылка на вакансию: {self.url}"
