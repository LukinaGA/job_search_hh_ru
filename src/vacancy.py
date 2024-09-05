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
        return cls(**vacancy_dict)

    def __str__(self):
        return f"{self.name} (ЗП {self.salary} руб). {self.description}. Ссылка на вакансию: {self.url}"

    def cast_to_object_list(self, vacancies: list[dict]) -> object:
        """Считывает данные из JSON-файла и на их основе создает объекты классов"""
        vacancies_list = []
        for vacancy in vacancies:
            name = vacancy.get("name")
            url = vacancy.get("alternate_url")
            description = vacancy.get('snippet').get('responsibility')
            if vacancy.get("salary"):
                if vacancy.get("salary").get("to"):
                    salary = vacancy.get("salary").get("to")
                elif vacancy.get("salary").get("from"):
                    salary = vacancy.get("salary").get("from")
            else:
                salary = 0

            vac = {"name": name, "url": url, "description": description, "salary": salary}
            vacancies_list.append(vac)

        return vacancies_list
    