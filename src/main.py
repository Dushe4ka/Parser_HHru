from src.api_src import HeadHunterAPI
from src.VacancyClass import Vacancy
from src.vacancy_saver import VacancySaver
from src.utils import filter_vacancies, get_top_vacancies, print_vacancies, \
    load_data
import json


def main():
    platforms = ["HeadHunter"]
    search_query = input("Введите поисковый запрос: ")
    # top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите точное название вакансии для фильтрации: ")
    salary_from = input("Введите цену от:")
    salary_to = input("Введите цену до:")
    """.split()"""
    # salary_range = input("Введите диапазон зарплат (пример: 100000-150000): ")

    hh_api = HeadHunterAPI()
    hh_vacancies = hh_api.get_vacancies(search_query)
    data = VacancySaver()
    data.add_vacancy(hh_vacancies)
    data = load_data()
    # for unit in data:
    #     list_products = [unit['name']]
    #     print(list_products)
    # print("Ответ API:", hh_vacancies['items'])  # Добавим вывод для отладки

    vacancies_list = []
    for vacancy in data:
        # print(vacancy)
        if isinstance(vacancy, dict):
            name = vacancy['name']
            alternate_url = vacancy['alternate_url']
            salary_info = vacancy['salary']
            if salary_info:
                salary_from = salary_info['from']
                salary_to = salary_info['to']
            else:
                salary_from = 'Зарплата не указана'
                salary_to = 'Зарплата не указана'
            try:
                description = vacancy['snippet']['responsibility']
            except:
                description = 'Описание отсутствует'
            vacancies_list.append({'name': name, 'alternate_url': alternate_url, 'salary_from': salary_from,
                                   'salary_to': salary_to,
                                   'description': description})

    # for i in vacancies_list:
    #     """
    #         Для отладки программы
    #     """
    #     print(i)

    # for vacancy in vacancies_list:
    #     if filter_words.lower() in vacancy['description']:
    #         print(vacancy)

    # if data and 'items' in data:
    #     vacancies_list = []
    #     for vacancy in data['items']:
    #         if isinstance(vacancy, dict):
    #             name = vacancy.get('name', 'Не указано')
    #             alternate_url = vacancy.get('alternate_url', 'Не указано')
    #
    #             # Обработка зарплаты
    #             salary_info = vacancy.get('salary')
    #             if salary_info:
    #                 salary_from = salary_info.get('from', 'Зарплата не указана')
    #             else:
    #                 salary_from = 'Зарплата не указана'
    #             description = vacancy.get('description', 'Описание отсутствует')
    #             vacancies_list.append({'name': name, 'alternate_url': alternate_url, 'salary_from': salary_from,
    #                                    'description': description})
    #         elif isinstance(vacancy, Vacancy):
    #             vacancies_list.append(vacancy)
    #
    #         print(vacancies_list)
    #
    #     filtered_vacancies = filter_vacancies(vacancies_list, filter_words)
    #     print(filtered_vacancies)
    #     ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)
    #     print(ranged_vacancies)
    #     sorted_vacancies = sort_vacancies(ranged_vacancies)
    #     print(sorted_vacancies)
    #     top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    #     print(top_vacancies)
    #     print_vacancies(top_vacancies)
    # else:
    #     print("Не удалось получить вакансии. Пожалуйста, проверьте запрос и попробуйте снова.")

    filtered_vacancies = filter_vacancies(vacancies_list, filter_words, salary_from, salary_to)
    # top_vacancies = get_top_vacancies(filtered_vacancies, top_n)
    # print(top_vacancies)
    # print_vacancies(filtered_vacancies)
    # for filter_vacancy in filtered_vacancies:
    #     print(filter_vacancy)
    print(filtered_vacancies)

    for v in filtered_vacancies:
        print(f"Название: {v.get('name', 'Не указано')}")


if __name__ == "__main__":
    main()
