from typing import List

from requests import request

EMPLOYEES = [1740, 1057, 15478, 3529, 2381, 633069, 2180, 78638, 4496, 5778059]


def get_vacancies_json_from_request(employer_param: List[int]) -> List[request]:
    url = "https://api.hh.ru/vacancies"
    params = {
        'area': range(1, 2),
        'page': range(5),
        'per_page': 100,
        'employer_id': employer_param
    }
    request_ = request(method='GET', url=url, params=params)
    return [
        [
            {
                'id': r['id'],
                'name': r['name'],
                'salary': r['salary']['from'] or r['salary']['to'],
                'description': r['snippet']['requirement'],
                'employee_id': r['employer']['id']
            }
        ] for r in request_.json()['items'] if r['salary']
    ]


def get_employees_json_from_request(employer_param: List) -> List[dict]:
    employees_list: List = []
    for employee_id in employer_param:
        url = 'https://api.hh.ru/employers/{}'.format(employee_id)
        request_ = request(method='GET', url=url).json()
        employees_list.append(request_)
    return [
        {
            'id': r['id'],
            'name': r['name']
        } for r in employees_list
    ]
45