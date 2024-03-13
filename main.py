from src.api_src import HeadHunterAPI
from src.VacancyClass import Vacancy
from src.vacancy_saver import VacancySaver
from src.utils import filter_vacancy, get_vacancies_by_salary, sort_vacancies, get_top_vacancies, print_vacancies

def main():
    platforms = ["HeadHunter"]
    search_query = input("Введите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    salary_range = input("Введите диапазон зарплат (пример: 100000-150000): ")

    hh_api = HeadHunterAPI()
    hh_vacancies = hh_api.get_vacancies(search_query)

    print("Ответ API:", hh_vacancies)  # Добавим вывод для отладки

    if hh_vacancies and 'items' in hh_vacancies:
        vacancies_list = []
        for vacancy in hh_vacancies['items']:
            name = vacancy.get('name', 'Не указано')
            alternate_url = vacancy.get('alternate_url', 'Не указано')

            # Обработка зарплаты
            salary_info = vacancy.get('salary')
            salary_from = salary_info.get('from') if salary_info else 'Зарплата не указана'

            description = vacancy.get('description', 'Описание отсутствует')
            vacancies_list.append(Vacancy(name, alternate_url, salary_from, description))

        filtered_vacancies = filter_vacancy(vacancies_list, filter_words)
        ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)
        sorted_vacancies = sort_vacancies(ranged_vacancies)
        top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
        print_vacancies(top_vacancies)
    else:
        print("Не удалось получить вакансии. Пожалуйста, проверьте запрос и попробуйте снова.")

if __name__ == "__main__":
    main()