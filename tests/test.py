from src.utils import filter_vacancies, get_top_vacancies, print_vacancies
from src.VacancyClass import Vacancy

vacancies_list = [
    {'name': 'Вакансия 1',
     'area': {'name': 'Москва'},
     'snippet': {'requirement': 'Высшее образование', 'responsibility': 'Работать'},
     'experience': {'name': '1 год'},
     'employer': {'name': 'ИП 1'},
     'salary': {'from': 30000, 'to': 0, 'currency': 'USD'},
     'alternate_url': 'hh.ru'},

    {'name': 'Вакансия 2',
     'area': {'name': 'Ижевск'},
     'snippet': {'requirement': 'Высшее образование', 'responsibility': 'Работать'},
     'experience': {'name': '2 года'},
     'employer': {'name': 'ИП 2'},
     'salary': {'from': 30000, 'to': 0, 'currency': 'USD'},
     'alternate_url': 'hh.ru'},

    {'name': 'Вакансия 3',
     'area': {'name': 'Новосибирск'},
     'snippet': {'requirement': 'Базовое образование', 'responsibility': 'Работать'},
     'experience': {'name': '3 годa'},
     'employer': {'name': 'ИП 3'},
     'salary': {'from': 0, 'to': 40000, 'currency': 'USD'},
     'alternate_url': 'hh.ru'}
]

filter_words = 'работать'

filtered_vacancy = Vacancy.from_json(vacancies_list)


def test_filter_vacancies():
    filtered_vacancies = filter_vacancies(filtered_vacancy, filter_words, 1000)
    assert filtered_vacancies == filtered_vacancy[0:2]

    filtered_vacancies = filter_vacancies(filtered_vacancy, '', 0)
    assert filtered_vacancies == filtered_vacancies

def test_get_top_vacancies():
    filtered_vacancies = get_top_vacancies(filtered_vacancy, None)
    assert filtered_vacancies == filtered_vacancy[:3]

    filtered_vacancies = get_top_vacancies(filtered_vacancy, 2)
    assert filtered_vacancies == filtered_vacancy[:2]

    filtered_vacancies = get_top_vacancies(filtered_vacancy, 5)
    assert filtered_vacancies == filtered_vacancy[:3]