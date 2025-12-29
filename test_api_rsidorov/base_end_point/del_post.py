import allure
import requests
from base_end_point.create_post import CreatePost


class DelPost(CreatePost):

    @allure.step('Delete post')
    def del_obj(self, headers=None):
        body_create = {"name": "create_for_update", "data": {"color": "blue", "size": "average"}}
        self.create_new_post(body_create)
        headers = headers if headers else self.headers
        self.response = requests.delete(f'{self.url}/{self.post_id}', headers=headers)
        return self.response
