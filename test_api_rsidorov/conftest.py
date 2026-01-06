import pytest

from base_end_point.create_post import CreatePost
from base_end_point.putch_post import PatchPost
from base_end_point.update_post import UpdatePost
from base_end_point.del_post import DelPost


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


@pytest.fixture()
def create_car(create_car_endpointe, del_new_car):
    body = {"name": "car", "data": {"color": "red", "size": "large"}}
    response = create_car_endpointe.create_new_car(body)
    post_data = response.json()
    post_id = post_data['id']
    yield post_data
    print(f"🗑 Удаляем объект с id={post_id}")
    del_new_car.del_obj(post_id)


@pytest.fixture()
def create_car_endpointe(start_stop, precond):
    return CreatePost()


@pytest.fixture()
def update_car(precond):
    return UpdatePost()


@pytest.fixture()
def del_new_car(precond):
    return DelPost()


@pytest.fixture()
def patch_new_car(precond):
    return PatchPost()
