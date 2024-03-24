from src.api_src import HeadHunterAPI
from src.VacancyClass import Vacancy
from src.vacancy_saver import VacancySaver
from src.utils import filter_vacancies, get_top_vacancies, print_vacancies, \
    load_data
import json


def main():
    platforms = ["HeadHunter"]
    search_query = input("Введите поисковый запрос: ")
    top_n = input("Введите количество вакансий для вывода в топ N: ")
    filter_words = input("Введите фильтры для отбора вакансии: ")
    salary_from = input("Введите зарплату от: ")

    hh_api = HeadHunterAPI()
    hh_vacancies = hh_api.get_vacancies(search_query)
    data = VacancySaver()
    data.add_vacancy(hh_vacancies)
    vacancies_from_json = load_data()

    vacancies_list = Vacancy.from_json(vacancies_from_json)

    # for vacancies in data:
    #     """
    #         Для отладки программы
    #     """
    #     print(vacancies)

    filtered_vacancies = filter_vacancies(vacancies_list, filter_words, salary_from)
    top_vacancy = get_top_vacancies(filtered_vacancies, top_n)
    print_vacancies(top_vacancy)

    # data.delete_vacancy()

if __name__ == "__main__":
    main()
