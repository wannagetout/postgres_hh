from typing import List

from db_connector import DBConnector


class DBManager(DBConnector):
    """
    Класс для передачи данных в БД
    """

    def __init__(self, info: List[dict]):
        super().__init__(info)

    def get_companies_and_vacancies_count(self):
        pass

    def get_all_vacancies(self):
        pass

    def get_avg_salary(self):
        pass

    def get_vacancies_with_higher_salary(self):
        pass

    def get_vacancies_with_keyword(self):
        pass