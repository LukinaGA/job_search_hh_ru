# Вакансии HeadHunter.ru

## Описание

Программа для получения информации о вакансиях с платформы hh.ru в России, сохранения ее в файл и удобной работы с ней: добавления, фильтрации и удаления.

## Содержание

* модули main.py и config.py в корне проекта
* папка data
* директория tests с тестами к модулям
* директория src с рабочими модулями

**Модули директории src:**
1. *head_hunter_api.py*. В модуле описан абстрактный класс Parser и класс HeadHunterAPI
```
class HeadHunterAPI(Parser):
    """Класс для работы с API HeadHunter"""

    def __init__(self) -> None:
        """Инициализатор класса HeadHunterAPI"""
        self.__url = "https://api.hh.ru/vacancies"
        self.__headers = {"User-Agent": "HH-User-Agent"}
        self.__params = {"text": "", "page": 0, "per_page": 100}
        self.__vacancies: list[dict] = []
```
Класс подключается к API hh.ru и возвращает список словарей с вакансиями

2. *saver.py*. В модуле описан абстрактный класс BaseSaver и класс JSONSaver для работы с вакансиями
```
class JSONSaver(BaseSaver):

    def __init__(self, filename: str = "vacancies.json") -> None:
        """Инициализатор класса JSONSaver"""
        self.__file_path = os.path.join(DATA_DIR, filename)
```

3. *utils.py*. Модуль содержит функции для сортировки и фильтрации вакансий (get_vacancies_by_salary_from, sort_vacancies_by_salary, get_top_vacancies)


4. *vacancy.py*. Модуль содержит класс Vacancy
```
    class Vacancy:
    """Класс для представления вакансий"""

    __slots__ = ("name", "url", "requirement", "responsibility", "salary")

    def __init__(self, name: str, url: str, requirement: str, responsibility: str,
                 salary: int | None = None) -> None
```

## Тестировние

В директории tests прописаны тесты для всех модулей директории src.
Также здесь есть модуль conftest.py с фикстурами для тестов. Coverage report: 84%