import requests
import pytest


@pytest.fixture(scope="session")
def start_stop():
    print("Start testing")
    yield
    print("Testing completed")


@pytest.fixture()
def precond():
    print("before test")
    yield
    print("after_test")


def test_one_get(start_stop, precond, new_post_del):
    post_id = new_post_del
    respomse = requests.get(f'http://objapi.course.qa-practice.com/object/{post_id}').json()
    assert respomse['id'] == post_id
    assert respomse['name'] == "test"


@pytest.fixture()
def new_post_del(precond):
    body = {
        "name": "test",
        "data": {
            "color": "blue",
            "size": "average"
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post('http://objapi.course.qa-practice.com/object', json=body, headers=headers)
    yield response.json()['id']
    post_id = response.json()['id']
    response = requests.delete(f'http://objapi.course.qa-practice.com/object/{post_id}')
    print(response.status_code)


@pytest.mark.parametrize("a", [
    {
        "name": "test",
        "data": {
            "color": "blue",
            "size": "average"
        }},
    {
        "name": "test1",
        "data": {
            "color": "blue",
            "size": "average"
        }},
    {
        "name": "test2",
        "data": {
            "color": "blue",
            "size": "average"
        }}
]
                         )
def test_post(precond, a):
    headers = {'Content-Type': 'application/json'}
    response = requests.post('http://objapi.course.qa-practice.com/object', json=a, headers=headers)
    assert response.json()["name"] == "test"


@pytest.mark.critical
def test_put_obj(precond, new_post_del):
    post_id = new_post_del
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


@pytest.mark.medium
def test_patch_obj(precond, new_post_del):
    post_id = new_post_del
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


def test_del_obj(precond, new_post_del):
    post_id = new_post_del
    response = requests.delete(f'http://objapi.course.qa-practice.com/object/{post_id}')
    print(response.status_code)
