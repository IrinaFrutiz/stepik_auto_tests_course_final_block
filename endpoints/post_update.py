import requests
import json
from endpoints.post_endpoint import Post
from config.data import Data


my_instance = Data()


class UpdateUsersPost(Post):
    path = '/post/'
    data = {
        "id": '659551257c13cd59d677a3af',
        "owner": "659417bfa26bc4984b1f76ea"
    }

    def new_object(self, data, without=False):
        if data:
            self.data.update(data)
        self.path += self.data["id"]
        self.data.update(my_instance.generate_users_post_data())
        if without:
            self.response = requests.put(self.URL + self.path, data=json.dumps(self.data))
        else:
            self.response = requests.put(self.URL + self.path, headers=self.headers, data=json.dumps(self.data))
        self.response_json = self.response.json()
