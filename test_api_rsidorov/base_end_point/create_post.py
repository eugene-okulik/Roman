import allure
import requests
from base_end_point.end_point import EndPoint


class CreatePost(EndPoint):
    post_id = None

    @allure.step('Create new posts')
    def create_new_car(self, body, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.post(self.url, json=body, headers=headers)
        self.json = self.response.json()
        print(f"🔧 Создан объект с id={self.json['id']}")
        return self.response
