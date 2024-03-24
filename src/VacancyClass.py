import json

class Vacancy:
    def __init__(self, title, link, salary, description):
        self.title = title
        self.link = link
        self.salary = salary
        self.description = description

        if not isinstance(self.title, (str, int, float)):
            self.salary = "Зарплата не указана"

    def __str__(self):
        return f"Название: {self.title}\nСсылка: {self.link}\nЗарплата: {self.salary}\nОписание: {self.description}\n"

    def __lt__(self, other):
        return self.salary < other.salary

    def to_json(self):
        return json.dumps(self.__dict__)

    @classmethod
    def from_json(cls, json_vacancy):
        vacancies_list = []
        for vacancy in json_vacancy:
            # print(vacancy)
            if isinstance(vacancy, dict):
                name = vacancy['name']
                alternate_url = vacancy['alternate_url']
                salary_info = vacancy['salary']
                if salary_info:
                    salary_from = salary_info['from']
                    salary_to = salary_info['to']
                else:
                    salary_from = 0
                    salary_to = 0
                try:
                    description = vacancy['snippet']['responsibility']
                except:
                    description = 'Описание отсутствует'
                vacancies_list.append({'name': name,
                                       'alternate_url': alternate_url,
                                       'salary_from': salary_from,
                                       'salary_to': salary_to,
                                       'description': description})
        return vacancies_list
