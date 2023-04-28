from typing import List

import psycopg2

from db_settings import CONNECT_PARAMS


class DBConnector:

    """
    Класс для взаимодействия с БД
    """

    CONNECTION = psycopg2.connect(
        host=CONNECT_PARAMS['host'],
        database=CONNECT_PARAMS['database'],
        user=CONNECT_PARAMS['user'],
        password=CONNECT_PARAMS['password']
    )

    def __init__(self, info: List[dict]):
        self.info = info

    def get_all_vacancies(self):
        with self.CONNECTION() as connection:
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM vacancies')
            connection.commit()

    def get_companies_and_vacancies_count(self):
        with self.CONNECTION() as connection:
            cursor = connection.cursor()
            vacancies_count = cursor.execute('SELECT COUNT(vacancy_id) FROM vacancies')
            employees_count = cursor.execute('SELECT COUNT(employee_id) FROM employees')
            return vacancies_count, employees_count

    def get_avg_salary(self):
        pass

    def get_vacancies_with_higher_salary(self):
        pass

    def get_vacancies_with_keyword(self):
        pass

    def add(self, info: List[dict]):
        with self.CONNECTION() as connection:
            cursor = connection.cursor()

