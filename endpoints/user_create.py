import json
import requests
import allure
from endpoints.user_endpoint import User
from config.data import Data


my_instance = Data()


class CreateUser(User):
    path = "/user/create"
    data = my_instance.generate_user_data()

    def new_object(self, without_data=False, without_auth=False):
        if without_auth:
            self.response = requests.post(self.URL+self.path)
        else:
            if without_data:
                self.response = requests.post(self.URL+self.path, headers=self.headers)
            else:
                self.response = requests.post(self.URL+self.path, data=json.dumps(self.data), headers=self.headers)
        self.response_json = self.response.json()
        if "id" in self.response_json:
            self.data["id"] = self.response_json["id"]

    @allure.title("Check errors when a response don't have data")
    def check_errors(self):
        assert self.response_json['error'] == "BODY_NOT_VALID", \
            f'Wrong error'
        assert self.response_json['data']['lastName'] == "Path `lastName` is required.", \
            f'Wrong lastname error in response'
        assert self.response_json['data']['firstName'] == "Path `firstName` is required.", \
            f'Wrong firstName error in response'
        assert self.response_json['data']['email'] == "Path `email` is required.", \
            f'Wrong email error in response'
