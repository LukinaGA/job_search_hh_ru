from src.utils import get_vacancies_by_salary_from
from src.vacancy import Vacancy


def test_get_vacancies_by_salary_from(vacancies_objects):
    assert get_vacancies_by_salary_from(vacancies_objects, 500000) == []
    assert get_vacancies_by_salary_from(vacancies_objects, 100000) == [
        Vacancy("Разработчик", "https://hh", "требования", "обязанности", 100000)]
    assert get_vacancies_by_salary_from(vacancies_objects, 0) == vacancies_objects
    assert get_vacancies_by_salary_from([], 1000000) == []