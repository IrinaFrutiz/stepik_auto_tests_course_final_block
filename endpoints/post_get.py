import requests
import json
import allure
from endpoints.post_endpoint import Post


class GetUsersPost(Post):
    path = '/post/'
    data = {
        "id": '65d4e11da404e3eb9d35d1b0',
        "image": "img_link",
        "likes": 100,
        'text': 'text',
        'owner': '659417bfa26bc4984b1f76ea'
    }

    def new_object(self, data, auth=False):
        if data:
            self.data = data
        self.path += self.data["id"]
        if auth:
            self.response = requests.get(self.URL+self.path, data=json.dumps(self.data))
        else:
            self.response = requests.get(self.URL+self.path, data=json.dumps(self.data), headers=self.headers)
        self.response_json = self.response.json()

    @allure.title("Check error when the post don't exist")
    def check_not_found_error(self):
        assert self.response_json['error'] == 'RESOURCE_NOT_FOUND', \
            f"{self.response_json['error']} is a wrong error"
