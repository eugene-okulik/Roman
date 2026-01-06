def test_create_car(create_car_endpointe):
    body = {"name": "car", "data": {"color": "blue", "size": "average"}}
    create_car_endpointe.create_new_car(body)
    create_car_endpointe.check_response_title_is_correct(body['name'])
    create_car_endpointe.check_that_status_is_200()


def test_put_a_car(create_car, update_car):
    post_id = create_car['id']
    body = {
        "name": "no_test",
        "data": {
            "color": "green",
            "size": "big"
        }
    }
    update_car.changing_a_car(post_id, body=body)
    update_car.check_that_status_is_200()


def test_patch_a_car(create_car, patch_new_car):
    post_id = create_car['id']
    body = {
        "name": "patch_test",
    }
    patch_new_car.patching_a_car(post_id, body=body)
    patch_new_car.check_that_status_is_200()
    patch_new_car.check_response_title_is_correct_patch(body['name'])


def test_del_a_car(create_car, del_new_car):
    post_id = create_car['id']
    del_new_car.del_obj(post_id)
    del_new_car.check_that_status_is_200()
