from utils import EMPLOYEES, get_vacancies_json_from_request, get_employees_json_from_request
from entities.base.db_connector import DBConnector


if __name__ == '__main__':
    TABLE_NAMES = {
        'vacancies': 'vacancies',
        'employees': 'employees'
    }

    connector = DBConnector()
    # connector.create_databases()
    # employees = get_employees_json_from_request(EMPLOYEES)
    # vacancies = get_vacancies_json_from_request(EMPLOYEES)
    # connector.add(employees, TABLE_NAMES['employees'])
    # connector.add(vacancies, TABLE_NAMES['vacancies'])

    while True:
        user_input = int(
            input(
                '1 - Все вакансии\n'
                '2 - Количество вакансий в компаниях\n'
                '3 - Средняя ЗП о всем вакансиям\n'
                '4 - Самые высокие ЗП\n'
                '5 - Вакансии по ключевому слову\n'
                '6 - Выход\n'
            )
        )
        if user_input == 1:
            all_vacancies = connector.get_all_vacancies()
            for vacancy in all_vacancies:
                print(vacancy)
        if user_input == 2:
            print(connector.get_companies_and_vacancies_count())
        if user_input == 3:
            print(connector.get_avg_salary())
        if user_input == 4:
            huge_salary = connector.get_vacancies_with_higher_salary()
            for vacancy in huge_salary:
                print(vacancy)
        if user_input == 5:
            word = input('Введите ключевое слово: ')
            keyword_vacancies = connector.get_vacancies_with_keyword(keyword=word)
            for vacancy in keyword_vacancies:
                print(vacancy)
        if user_input == 6:
            exit()
