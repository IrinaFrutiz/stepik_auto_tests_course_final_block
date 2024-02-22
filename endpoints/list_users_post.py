import requests
from endpoints.lists_endpoint import List


class GetUsersPostList(List):
    path = '/user/'
    data = {
        "id": "659417bfa26bc4984b1f76ea"
    }

    def new_object(self, data, without=False):
        if data:
            self.data = data
        self.path += self.data["id"] + '/post'
        if without:
            self.response = requests.get(self.URL+self.path)
        else:
            self.response = requests.get(self.URL+self.path, headers=self.headers)
        self.response_json = self.response.json()
