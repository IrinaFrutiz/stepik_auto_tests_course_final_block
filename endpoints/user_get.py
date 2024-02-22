import requests
import allure
from endpoints.user_endpoint import User


class GetUser(User):
    path = "/user/"
    data = {
        "id": "658d761f1d2a3818e95b55fb",
        "firstName": "Laura",
        "lastName": "Moran",
        "email": "thompsonnicholas@example.com"
    }

    def new_object(self, data, auth=False):
        if data:
            self.data = data
        if auth:
            self.response = requests.get(self.URL + self.path + self.data["id"])
        else:
            self.response = requests.get(self.URL+self.path+self.data["id"], headers=self.headers)
        self.response_json = self.response.json()

    @allure.title("Check error when the user don't exist")
    def check_not_found_error(self):
        assert self.response_json['error'] == 'RESOURCE_NOT_FOUND', \
            f"{self.response_json['error']} is a wrong error"
