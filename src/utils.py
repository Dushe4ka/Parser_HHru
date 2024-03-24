import os
import json


def load_data():
    ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
    PATH = os.path.join(ROOT_DIR, 'src', 'vacancies.json')
    with open(PATH, encoding='UTF-8') as f:
        data = json.load(f)
        return data


def filter_vacancies(vacations_list, words=None, salary_from='Зарплата не указана', salary_to='Зарплата не указана'):
    filtered_objects = []

    for vacation in vacations_list:
        if words is not None and vacation['name'] != words:
            continue
        elif words is None:
            continue
        if salary_from is not None and vacation['salary_from'] < salary_from:
            continue
        if salary_to is not None and vacation['salary_to'] > salary_to:
            continue

        filtered_objects.append(vacation)

    return filtered_objects


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
        for vacancy in vacancies_list:
            print(f"Название: {vacancy.get('name', 'Не указано')}")
            print(f"Зарплата от: {vacancy.get('salary_from', 'Не указана')}")
            print(f"Описание: {vacancy.get('description', 'Отсутствует')}")
            print(f"Ссылка: {vacancy.get('alternate_url', 'Не указана')}")
            print()
    else:
        print("Вакансии отсутствуют")
    # if vacancies_list:
    #     for index, vacancy in enumerate(vacancies_list, start=1):
    #         print(f"Вакансия {index}:")
    #         print(f"Название: {vacancy.get('name', 'Не указано')}")
    #         print(f"Зарплата от: {vacancy.get('salary_from', 'Не указана')}")
    #         print(f"Описание: {vacancy.get('description', 'Отсутствует')}")
    #         print(f"Ссылка: {vacancy.get('alternate_url', 'Не указана')}")
    #         print()
    # else:
    #     print("Вакансии отсутствуют")