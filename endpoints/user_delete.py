import requests
from endpoints.user_endpoint import User


class DeleteUser(User):
    path = "/user/"
    data = {}

    def new_object(self, data, auth=False):
        self.data.update(data)
        self.path += self.data['id']
        if auth:
            self.response = requests.delete(self.URL+self.path)
        else:
            self.response = requests.delete(self.URL+self.path, headers=self.headers)
        self.response_json = self.response.json()
