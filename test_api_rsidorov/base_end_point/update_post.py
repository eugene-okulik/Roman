import allure
import requests
from base_end_point.create_post import CreatePost


class UpdatePost(CreatePost):

    @allure.step('Update a post')
    def changing_a_post(self, headers=None, body=None):
        body_create = {"name": "create_for_update", "data": {"color": "blue", "size": "average"}}
        self.create_new_post(body_create)
        headers = headers if headers else self.headers
        self.response = (requests.put
            (
            f'{self.url}/{self.post_id}',
            json=body,
            headers=headers
        )
        )
        return self.response
