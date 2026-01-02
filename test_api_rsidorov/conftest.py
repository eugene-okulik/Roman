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
def create_car():
    body = {"name": "car", "data": {"color": "red", "size": "large"}}
    creator = CreatePost()
    response = creator.create_new_car(body)
    post_data = response.json()
    return post_data

@pytest.fixture()
def create_post_endpointe(start_stop, precond):
    return CreatePost()


@pytest.fixture()
def update_post(precond, create_post_endpointe):
    return UpdatePost()


@pytest.fixture()
def del_new_post(precond):
    return DelPost()


@pytest.fixture()
def patch_new_post(precond):
    return PatchPost()
