from utils import EMPLOYEES, get_vacancies_json_from_request, get_employees_json_from_request
from entities.base.db_connector import DBConnector


if __name__ == '__main__':
    TABLE_NAMES = {
        'vacancies': 'vacancies',
        'employees': 'employees'
    }

    connector = DBConnector()
    connector.create_databases()
    employees = get_employees_json_from_request(EMPLOYEES)
    vacancies = get_vacancies_json_from_request(EMPLOYEES)
    connector.add(employees, TABLE_NAMES['employees'])
    connector.add(vacancies, TABLE_NAMES['vacancies'])

    all_vac = connector.get_all_vacancies()
    print(all_vac)
