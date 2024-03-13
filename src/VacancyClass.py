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

    
