import requests
from abc import ABC, abstractmethod


class AbstractAPI(ABC):
    @abstractmethod
    def get_vacancies(self, key_word):
        pass


class HeadHunterAPI(AbstractAPI):
    def __init__(self):
        self.url = "https://api.hh.ru/vacancies"

    def get_vacancies(self, key_word):
        params = {"text": key_word, "area": 1}
        response = requests.get(self.url, params=params)
        return response.json()
