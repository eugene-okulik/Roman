import allure


class EndPoint:
    url = 'http://objapi.course.qa-practice.com/object'
    response = None
    json = None
    headers = {'Content-Type': 'application/json'}

    @allure.step('Check that title is the same as sent')
    def check_response_title_is_correct(self, car):
        assert self.json['name'] == car, 'Uncorrected name'

    @allure.step('Check that response is 200')
    def check_that_status_is_200(self):
        assert self.response.status_code == 200, 'Status not 200'

    @allure.step('Check that 400 error received')
    def check_bad_request(self):
        assert self.response.status_code == 400, 'Status not 400'

    @allure.step('Check that title update after PATCH')
    def check_response_title_is_correct_patch(self, patch_test):
        assert self.json['name'] == patch_test, 'Uncorrected name'
