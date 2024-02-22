import requests
import json
from endpoints.post_endpoint import Post
from config.data import Data


my_instance = Data()


class CreateUsersPost(Post):
    path = '/post/create'
    data = {
        'owner':  '659417bfa26bc4984b1f76ea'
    }

    def new_object(self, owner, without=False):
        if owner:
            self.data["owner"] = owner
        self.data.update(my_instance.generate_users_post_data())
        if without:
            self.response = requests.post(self.URL+self.path, data=json.dumps(self.data))
        else:
            self.response = requests.post(self.URL+self.path, headers=self.headers, data=json.dumps(self.data))
        self.response_json = self.response.json()

    def check_not_found_error(self):
        assert self.response_json['error'] == "BODY_NOT_VALID", \
                f'Wrong error in response'
