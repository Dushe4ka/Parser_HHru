from abc import ABC, abstractmethod
import json


class AbstractVacancySaver(ABC):
    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy):
        pass

    @abstractmethod
    def get_vacancy_by_filter(self, filters):
        pass


class VacancySaver(AbstractVacancySaver):
    def __init__(self, file_path="vacancies.json"):
        self.file_path = file_path

    def add_vacancy(self, vacancy):
        vacancy.pop()
        """Добавление вакансии в файл"""
        with open(self.file_path, 'a') as file:
            json.dump(vacancy, file, indent=2)
            file.write("\n")

    def delete_vacancy(self, vacancy):
        """Заглушка для удаления вакансии из файла"""
        pass

    def get_vacancy_by_filter(self, filters):
        """Заглушка для поиска вакансий по фильтру"""
        pass
