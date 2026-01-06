import allure
import requests
from base_end_point.end_point import EndPoint


class DelPost(EndPoint):

    @allure.step('Delete post')
    def del_obj(self, post_id, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.delete(f'{self.url}/{post_id}', headers=headers)
        return self.response
