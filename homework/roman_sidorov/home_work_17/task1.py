import requests


def one_get():
    post_id = post()
    respomse = requests.get(f'http://objapi.course.qa-practice.com/object/{post_id}').json()
    assert respomse['id'] == post_id
    assert respomse['name'] == "test"


def post():
    body = {
        "name": "test",
        "data": {
            "color": "blue",
            "size": "average"
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post('http://objapi.course.qa-practice.com/object', json=body, headers=headers)
    return response.json()['id']


def put_obj():
    post_id = post()
    body = {
        "name": "no_test",
        "data": {
            "color": "green",
            "size": "big"
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.put(f'http://objapi.course.qa-practice.com/object/{post_id}', json=body, headers=headers).json()
    assert response['name'] == 'no_test'


def patch_obj():
    post_id = post()
    body = {
        "data": {
            "color": "green",
            "size": "big"
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(f'http://objapi.course.qa-practice.com/object/{post_id}', json=body,
                              headers=headers).json()
    assert response['name'] == 'test', 'Incorrect name'


def del_obj():
    post_id = post()
    response = requests.delete(f'http://objapi.course.qa-practice.com/object/{post_id}')
    print(response.status_code)
