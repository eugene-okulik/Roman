def test_post(create_post_endpointe):
    body = {"name": "test", "data": {"color": "blue", "size": "average"}}
    create_post_endpointe.create_new_post(body)
    create_post_endpointe.check_response_title_is_correct(body['name'])
    create_post_endpointe.check_that_status_is_200()

def test_put_a_post(update_post):
    body = {
        "name": "no_test",
        "data": {
            "color": "green",
            "size": "big"
        }
    }
    update_post.changing_a_post(body=body)
    update_post.check_that_status_is_200()

def test_patch_a_post(patch_new_post):
    body = {
        "name": "patch_test",
    }
    patch_new_post.patching_a_post(body=body)
    patch_new_post.check_that_status_is_200()
    patch_new_post.check_response_title_is_correct_patch(body['name'])

def test_del_a_post(del_new_post):
    del_new_post.del_obj()
    del_new_post.check_that_status_is_200()