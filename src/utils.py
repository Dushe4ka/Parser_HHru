import os
import json


def load_data():
    ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
    PATH = os.path.join(ROOT_DIR, 'src', 'vacancies.json')
    with open(PATH, encoding='UTF-8') as f:
        data = json.load(f)
        return data


def filter_vacancies(vacations_list, words=None, salary_from=None):
    filtered_objects = []

    for vacation in vacations_list:
        if vacation['description'].lower().count(words):
            if int(vacation['salary_from']) >= int(salary_from):
                filtered_objects.append(vacation)


    return filtered_objects


def get_top_vacancies(sorted_vacancies, top_n):
    """
    Получаем первые top_n вакансий
    :param sorted_vacancies:
    :param top_n:
    :return:
    """
    if not top_n:
        top_n = len(sorted_vacancies)
        top_vacancies = sorted_vacancies[:top_n]
        return top_vacancies

    try:
        top_n = int(top_n)
        if len(sorted_vacancies) < top_n:
            top_n = len(sorted_vacancies)

        top_vacancies = sorted_vacancies[:top_n]
        return top_vacancies
    except:
        pass


def print_vacancies(vacancies_list):
    """
    Печатаем вакансии
    :param vacancies_list:
    :return:
    """
    if vacancies_list:
        for vacancy in vacancies_list:
            print()
            print(f"Название: {vacancy.get('name', 'Не указано')}")
            print(f"Зарплата от: {vacancy.get('salary_from', 'Не указана')}")
            print(f"Описание: {vacancy.get('description', 'Отсутствует')}")
            print(f"Ссылка: {vacancy.get('alternate_url', 'Не указана')}")
            print()
    else:
        print("Вакансии отсутствуют")

