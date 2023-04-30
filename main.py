from utils import EMPLOYEES, get_vacancies_json_from_request, get_employees_json_from_request
from entities.manager.db_manager import DBManager


if __name__ == '__main__':
    TABLE_NAMES = {
        'vacancies': 'vacancies',
        'employees': 'employees'
    }

    employees = get_employees_json_from_request(EMPLOYEES)
    vacancies = get_vacancies_json_from_request(EMPLOYEES)
    db_vacancies = DBManager(vacancies)
    db_employees = DBManager(employees)
    db_employees.add_entities(TABLE_NAMES['employees'])
    db_vacancies.add_entities(TABLE_NAMES['vacancies'])

    db_vacancies.get_vacancies()
