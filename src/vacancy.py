class Vacancy:
    """Класс для представления вакансий"""
    __slots__ = ("name", "url", "description", "salary")

    def __init__(self, name: str, url: str, description: str, salary=None):
        self.name = name
        self.url = url
        self.description = description
        try:
            self.salary = self.__salary_validation(salary)
        except TypeError as te:
            self.salary = 0
            print(f"{te}, будет указано значение по умолчанию (0)")

    @staticmethod
    def __salary_validation(salary: float):
        if salary:
            if type(salary) == float:
                return salary
            raise TypeError("Зарплата должна быть числом")
        return 0

    @classmethod
    def new_vacancy(cls, vacancy_dict: dict) -> "Vacancy":
        """Создаёт новый экземпляр класса Vacancy из словаря"""
        return cls(**vacancy_dict)

    def __str__(self):
        return f"{self.name} (ЗП {self.salary} руб). {self.description}. Ссылка на вакансию: {self.url}"

    @classmethod
    def __verify_data(cls, other):
        if not isinstance(other, (float, Vacancy)):
            raise TypeError

        return other if isinstance(other, float) else other.salary

    def __eq__(self, other):
        sal = self.__verify_data(other)
        return self.salary == sal

    def __lt__(self, other):
        sal = self.__verify_data(other)
        return self.salary < sal

    def __lg__(self, other):
        sal = self.__verify_data(other)
        return self.salary <= sal

    def cast_to_object_list(self, vacancies: list[dict]) -> object:
        """Возвращает список словарей с данными о вакансиях с ключами name, url, description, salary"""
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
