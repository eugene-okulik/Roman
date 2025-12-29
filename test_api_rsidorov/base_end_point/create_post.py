import allure
import requests
from base_end_point.end_point import EndPoint


class CreatePost(EndPoint):
    post_id = None

    @allure.step('Create new post')
    def create_new_post(self, body, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.post(self.url, json=body, headers=headers)
        self.json = self.response.json()
        self.post_id = self.json['id']
        print(self.post_id)
        return self.response
