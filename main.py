import requests

def get_vacancies(keyword):
    url = "https://api.hh.ru/vacancies"
    params = {
        "text": keyword,
        "area": 1,  # Specify the desired area ID (1 is Moscow)Можно выбрать другой area ID (1 - Москва)
        "per_page": 10,  # Количество вакансий на странице
    }
    headers = {
        "User-Agent": "Your User Agent",  # Replace with your User-Agent header
    }

    response = requests.get(url, params=params, headers=headers)

    if response.status_code == 200:
        data = response.json()
        vacancies = data.get("items", [])
        for vacancy in vacancies:
            # Extract relevant information from the vacancy object
            vacancy_id = vacancy.get("id")
            vacancy_title = vacancy.get("name")
            vacancy_price = vacancy.get("compensation")
            vacancy_url = vacancy.get("alternate_url")
            company_name = vacancy.get("employer", {}).get("name")
            print(f"ID: {vacancy_id}\nTitle: {vacancy_title}\nCompany: {company_name}\nURL: {vacancy_url}\nprice: {vacancy_price}\n")
    else:
        print(f"Request failed with status code: {response.status_code}")

xeca = input("Введите фильтр: ")
# Example usage
get_vacancies(xeca)