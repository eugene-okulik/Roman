from locust import task, HttpUser, tag



class CudCar(HttpUser):

    def on_start(self):
        body = {"name": "car", "data": {"color": "blue", "size": "average"}}
        self.headers = {'Content-Type': 'application/json'}
        response = self.client.post('/object', json=body, headers=self.headers)
        self.post_id = response.json()['id']
        print(f'Объект {self.post_id} создан')

    def on_stop(self):
        self.client.delete(f'/object/{self.post_id}',  headers=self.headers)
        print(f'Объект {self.post_id} удален')

    @tag('critpath')
    @task
    def create_new_cars(self):
        update_body = {
            "name": "no_test",
            "data": {
                "color": "green",
                "size": "big"
            }
        }
        self.client.put(f'/object/{self.post_id}', json=update_body, headers=self.headers)
        patch_body = {"name": "patch_test"}
        self.client.patch(f'/object/{self.post_id}', json=patch_body, headers=self.headers)

    @tag('smoke')
    @task
    def create_new_cars(self):
        update_body = {
            "name": "no_test",
            "data": {
                "color": "green",
                "size": "big"
            }
        }
        self.client.put(f'/object/{self.post_id}', json=update_body, headers=self.headers)
        patch_body = {"name": "patch_test"}
