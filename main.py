from src.api_src import HeadHunterAPI
from src.VacancyClass import Vacancy
from src.vacancy_saver import VacancySaver
from src.utils import filter_vacancies, get_vacancies_by_salary, sort_vacancies, get_top_vacancies, print_vacancies
import json


def main():
    platforms = ["HeadHunter"]
    search_query = input("Введите поисковый запрос: ")
    # top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    # filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    # salary_range = input("Введите диапазон зарплат (пример: 100000-150000): ")

    hh_api = HeadHunterAPI()
    hh_vacancies = hh_api.get_vacancies(search_query)
    data = VacancySaver()
    for vacancy in hh_vacancies['items']:

        data.add_vacancy(vacancy)



    print("Ответ API:", hh_vacancies['items'])  # Добавим вывод для отладки

    # if hh_vacancies and 'items' in hh_vacancies:
    #     vacancies_list = []
    #     for vacancy in hh_vacancies['items']:
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


if __name__ == "__main__":
    main()
