import allure
import requests
from base_end_point.end_point import EndPoint


class UpdatePost(EndPoint):

    @allure.step('Update a post')
    def changing_a_car(self, post_id, headers=None, body=None):
        headers = headers if headers else self.headers
        self.response = (requests.put(f'{self.url}/{post_id}', json=body, headers=headers))
        return self.response
