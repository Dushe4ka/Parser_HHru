from abc import ABC, abstractmethod
import os
import json


class AbstractVacancySaver(ABC):
    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def delete_vacancy(self):
        pass


class VacancySaver(AbstractVacancySaver):
    def __init__(self, file_path="vacancies.json"):
        self.file_path = file_path

    def add_vacancy(self, vacancy):
        """Добавление вакансии в файл"""
        with open(self.file_path, 'a') as file:
            json.dump(vacancy.get("items", []), file, indent=2)
            # file.write("\n")

    def delete_vacancy(self):
        """Заглушка для удаления вакансии из файла"""
        open(self.file_path, 'w').close()
        os.remove(self.file_path)
