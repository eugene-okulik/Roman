def test_create_car(create_post_endpointe):
    body = {"name": "car", "data": {"color": "blue", "size": "average"}}
    create_post_endpointe.create_new_car(body)
    create_post_endpointe.check_response_title_is_correct(body['name'])
    create_post_endpointe.check_that_status_is_200()


def test_put_a_car(create_car, update_post):
    post_id = create_car['id']
    body = {
        "name": "no_test",
        "data": {
            "color": "green",
            "size": "big"
        }
    }
    update_post.changing_a_car(post_id, body=body)
    update_post.check_that_status_is_200()


def test_patch_a_car(create_car, patch_new_post):
    post_id = create_car['id']
    body = {
        "name": "patch_test",
    }
    patch_new_post.patching_a_car(post_id, body=body)
    patch_new_post.check_that_status_is_200()
    patch_new_post.check_response_title_is_correct_patch(body['name'])


def test_del_a_car(create_car, del_new_post):
    post_id = create_car['id']
    del_new_post.del_obj(post_id)
    del_new_post.check_that_status_is_200()
