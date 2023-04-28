from typing import List

from db_connector import DBConnector

from utils import get_vacancies_json_from_request


class DBManager(DBConnector):
    """
    Класс для передачи данных в БД
    """

    def __init__(self, info: List[dict]) -> None:
        super().__init__(info)
        self.info = info

    def get_companies_and_vacancies_count(self) -> dict:
        vacancies = self.get_companies_and_vacancies_count()
        return vacancies

    def get_all_vacancies(self) -> dict:
        vacancies = self.get_all_vacancies()
        return vacancies

    def get_avg_salary(self) -> dict:
        vacancies = self.get_avg_salary()
        return vacancies

    def get_vacancies_with_higher_salary(self) -> dict:
        vacancies = self.get_vacancies_with_higher_salary()
        return vacancies

    def get_vacancies_with_keyword(self, keyword: str = 'Python') -> dict:
        vacancies = self.get_vacancies_with_keyword(keyword)
        return vacancies

    def add_vacancies(self, table_name: str) -> None:
        self.add(self.info, table_name)
