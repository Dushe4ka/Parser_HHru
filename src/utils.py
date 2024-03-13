import re

def get_salary(vacansy):
    """
    Получаем зарплату вакансии
    :param vacansy:
    :return:
    """
    salary = vacansy.salary

    if '-' in salary:
        """
        Если есть зарплата от-до то считаем среднюю
        """
        min_salary, max_salary = map(int, re.findall(r'\d+', salary))
        return (min_salary + max_salary) / 2
    elif salary.isdigit():
        """
        Если просто ЗП то сразу выводим
        """
        return int(salary)
    else:
        return 0

def filter_vacancy(vacancies_list, filter_words):
    """
    фильтр вакансий по ключевым словам
    :param vacancies_list:
    :param filter_words:
    :return:
    """
    filtered_vacancies = []
    for vacancy in vacancies_list:
        description_lower = vacancy.description.lower()
        if any(keyword.lower() in description_lower for keyword in filter_words):
            filtered_vacancies.append(vacancy)
    return filtered_vacancies

def get_vacancies_by_salary(vacancies, salary_range):
    """
    Получаем вакансии по зарплате
    :param vacancies:
    :param salary_range:
    :return:
    """
    if '-' in salary_range:
        min_salary, max_salary = map(int, salary_range.split('-'))
        return [vacancy for vacancy in vacancies if min_salary <= get_salary(vacancy) <= max_salary]
    else:
        return vacancies

def sort_vacancies(vacancies_list):
    """
    Сортировка вакансий по зарплате
    :param vacancies_list:
    :return:
    """
    sorted_vacancies = sorted(vacancies_list, key=lambda x: get_salary(x), reverse=True)
    return sorted_vacancies

def get_top_vacancies(vacancies, top_n):
    """
    Получаем первые top_n вакансий
    :param vacancies:
    :param top_n:
    :return:
    """
    return vacancies[:top_n]

def print_vacancies(vacancies_list):
    """
    Печатаем вакансии
    :param vacancies_list:
    :return:
    """
    for vacancy in vacancies_list:
        print(vacancy)