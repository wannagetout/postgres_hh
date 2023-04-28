from typing import List

import psycopg2

from db_settings import CONNECT_PARAMS


class DBConnector:

    """
    Класс для взаимодействия с БД
    """

    CONNECTION = psycopg2.connect(
        host=CONNECT_PARAMS["ost"],
        database=CONNECT_PARAMS["database"],
        user=CONNECT_PARAMS["user"],
        password=CONNECT_PARAMS["password"]
    )

    def __init__(self, info: List[dict]):
        self.info = info

    def get_all_vacancies(self):
        with self.CONNECTION() as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM vacancies")
            connection.commit()

    def get_companies_and_vacancies_count(self):
        with self.CONNECTION() as connection:
            cursor = connection.cursor()
            vacancies_count = cursor.execute("SELECT COUNT(vacancy_id) FROM vacancies")
            employees_count = cursor.execute("SELECT COUNT(employee_id) FROM employees")
            return vacancies_count, employees_count

    def get_avg_salary(self):
        with self.CONNECTION() as connection:
            cursor = connection.cursor()
            avg_salary = cursor.execute("SELECT AVG(salary) FROM vacancies")
            return avg_salary

    def get_vacancies_with_higher_salary(self):
        with self.CONNECTION() as connection:
            cursor = connection.cursor()
            highest_salary = cursor.execute(
                "SELECT * FROM vacancies ORDER BY salary DESC LIMIT 10"
            )
            return highest_salary

    def get_vacancies_with_keyword(self, keyword: str) -> str:
        with self.CONNECTION() as connection:
            cursor = connection.cursor()
            vacancies_with_keyword = cursor.execute(
                "SELECT * FROM vacancies WHERE name LIKE '%{}' ORDER BY name".format(keyword)
            )
            return vacancies_with_keyword

    def add(self, info: List[dict], table_name: str) -> None:
        with self.CONNECTION() as connection:
            cursor = connection.cursor()
            if table_name == 'employees':
                for employee in info:
                    cursor.execute("INSERT INTO employees(employee_id, name)"
                                   " VALUES ({}, {})".format(employee['id'], employee['name']))
            if table_name == 'vacancies':
                for vacancy in info:
                    cursor.execute(
                        "INSERT INTO vacancies(vacancy_id, name, salary, description, employee_id)"
                        " VALUES ({}, {}, {}, {}, {})"
                        "".format(vacancy['id'],
                                  vacancy['name'],
                                  vacancy['salary'],
                                  vacancy['description'],
                                  vacancy['employee_id']
                                  )
                    )
