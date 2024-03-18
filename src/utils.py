def filter_vacancies(vacancies, key_words):
    return [vacancy for vacancy in vacancies if
            any(key.lower() in vacancy['description'].lower() for key in key_words)]




def get_vacancies_by_salary(vacancies, salary_range):
    if not salary_range:
        return vacancies
    salary_range = salary_range.split('-')
    if len(salary_range) == 1:
        min_salary = max_salary = int(salary_range[0])
    elif len(salary_range) == 2:
        min_salary, max_salary = map(int, salary_range)
    else:
        print("Неверный формат диапазона зарплат.")
        return vacancies

    return [vacancy for vacancy in vacancies if
            vacancy.get('salary_from', 0) >= min_salary and
            vacancy.get('salary_from', float('inf')) <= max_salary]

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
    if vacancies_list:
        for index, vacancy in enumerate(vacancies_list, start=1):
            print(f"Вакансия {index}:")
            print(f"Название: {vacancy.get('name', 'Не указано')}")
            print(f"Зарплата от: {vacancy.get('salary_from', 'Не указана')}")
            print(f"Описание: {vacancy.get('description', 'Отсутствует')}")
            print(f"Ссылка: {vacancy.get('alternate_url', 'Не указана')}")
            print()
    else:
        print("Вакансии отсутствуют")