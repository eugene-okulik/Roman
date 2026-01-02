import allure
import requests
from base_end_point.end_point import EndPoint


class PatchPost(EndPoint):

    @allure.step('Short update a post')
    def patching_a_car(self, post_id, headers=None, body=None):
        headers = headers if headers else self.headers
        self.response = (requests.patch(f'{self.url}/{post_id}', json=body, headers=headers))
        self.json = self.response.json()
        return self.response
