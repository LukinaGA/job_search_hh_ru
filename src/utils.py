def get_vacancies_by_salary_range(vacancies: list[dict], salary_from: int, salary_to: int) -> list[dict]:
    """Возвращает список вакансий в заданном диапазоне зарплат"""
    return [vac for vac in vacancies if salary_from <= vac["salary"] <= salary_to]


def sort_vacancies_by_salary(vacancies: list[dict]) -> list[dict]:
    """Сортирует вакансии по зарплате"""
    return sorted(vacancies, key=lambda vacancy: vacancy["salary"], reverse=True)


def get_top_vacancies(vacancies: list[dict], top_n: int) -> list[dict]:
    """Возвращает топ n вакансий по зарплате"""
    sorted_vacancies = sort_vacancies_by_salary(vacancies)

    return sorted_vacancies[:top_n]
