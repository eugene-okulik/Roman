import allure
import requests
from base_end_point.create_post import CreatePost


class PatchPost(CreatePost):

    @allure.step('Short update a post')
    def patching_a_post(self, headers=None, body=None):
        body_create = {"name": "create_for_update", "data": {"color": "blue", "size": "average"}}
        self.create_new_post(body_create)
        headers = headers if headers else self.headers
        self.response = (requests.patch
            (
            f'{self.url}/{self.post_id}',
            json=body,
            headers=headers
        )
        )
        self.json = self.response.json()
        return self.response
