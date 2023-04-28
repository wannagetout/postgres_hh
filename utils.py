from typing import List

from requests import request

EMPLOYEES = [1740, 1057, 15478, 3529, 2381, 633069, 2180, 78638, 4496, 5778059]


def get_json_from_request(employer_param: List[int]) -> List[request]:
    url = "https://api.hh.ru/vacancies"
    params = {
        'area': range(1, 2),
        'page': range(5),
        'per_page': 100,
        'employer_id': employer_param
    }
    request_ = request(method='GET', url=url, params=params)
    return [r for r in request_.json()['items']]
