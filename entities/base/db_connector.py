from configparser import ConfigParser

from typing import List

import psycopg2


class DBConnector:

    """
    Класс для взаимодействия с БД
    """

    config = ConfigParser()
    config.read('database.ini')
    db = {}
    params = config.items('postgresql')
    for param in params:
        db[param[0]] = param[1]

    def __init__(self):
        self.info = None

    def get_all_vacancies(self):
        connection = psycopg2.connect(**self.db)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM vacancies;")
        vacancies = cursor.fetchall()
        connection.commit()
        connection.close()
        return vacancies

    def get_companies_and_vacancies_count(self):
        connection = psycopg2.connect(**self.db)
        cursor = connection.cursor()
        cursor.execute(
            "SELECT employee_id, COUNT(vacancy_id) "
            "FROM vacancies "
            "GROUP BY employee_id;")
        vacancies_count = cursor.fetchall()
        connection.commit()
        connection.close()
        return vacancies_count

    def get_avg_salary(self):
        connection = psycopg2.connect(**self.db)
        cursor = connection.cursor()
        cursor.execute("SELECT CEILING(AVG(salary)) as AVG_SALARY FROM vacancies;")
        avg_salary = cursor.fetchall()
        connection.commit()
        connection.close()
        return avg_salary

    def get_vacancies_with_higher_salary(self):
        connection = psycopg2.connect(**self.db)
        cursor = connection.cursor()
        cursor.execute(
            "SELECT * FROM vacancies ORDER BY salary DESC LIMIT 10;"
        )
        highest_salary = cursor.fetchall()
        connection.commit()
        connection.close()
        return highest_salary

    def get_vacancies_with_keyword(self, keyword: str) -> dict:
        connection = psycopg2.connect(**self.db)
        cursor = connection.cursor()
        cursor.execute(
            "SELECT * FROM vacancies WHERE name LIKE '%{}%' ORDER BY name".format(keyword)
        )
        vacancies_with_keyword = cursor.fetchall()
        connection.close()
        return vacancies_with_keyword

    def add(self, info: List[dict], table_name: str) -> None:
        connection = psycopg2.connect(**self.db)
        cursor = connection.cursor()
        if table_name == 'employees':
            for employee in info:
                cursor.execute("INSERT INTO employees(employee_id, name)"
                               " VALUES ({}, '{}')".format(employee['id'], employee['name']))
                connection.commit()
        if table_name == 'vacancies':
            for vacancy in info:
                cursor.execute(
                    "INSERT INTO vacancies(vacancy_id, name, salary, description, employee_id)"
                    " VALUES ({}, '{}', {}, '{}', {}) ON CONFLICT DO NOTHING;"
                    "".format(vacancy['id'],
                              vacancy['name'],
                              vacancy['salary'],
                              vacancy['description'],
                              vacancy['employee_id']
                              )
                )
                connection.commit()

    def create_databases(self) -> None:
        connection = psycopg2.connect(**self.db)
        try:
            cursor = connection.cursor()
            cursor.execute("CREATE TABLE employees "
                           "(employee_id INTEGER PRIMARY KEY, "
                           "name VARCHAR(80));"
                           )
            connection.commit()
            cursor.execute("CREATE TABLE vacancies"
                           "(vacancy_id INTEGER PRIMARY KEY,"
                           "name VARCHAR(150),"
                           "salary INTEGER,"
                           "description text,"
                           "employee_id INTEGER REFERENCES employees(employee_id));"
                           )
            connection.commit()
            connection.close()
        except:
            connection.rollback()

            cursor = connection.cursor()
            print('Таблицы уже существуют и были очищены')
            cursor.execute("TRUNCATE table vacancies;")
            connection.commit()
            cursor.execute("TRUNCATE table employees CASCADE;")
            connection.commit()
            connection.close()
