import json
import requests
import allure
from endpoints.user_endpoint import User
from config.data import Data


my_instance = Data()


class UpdateUser(User):
    path = "/user/"
    data = {
        "id": "659417bfa26bc4984b1f76ea",
        "email": "johnsonerica@example.com"
    }

    @allure.title("Put requests user update")
    def new_object(self, data, without_auth=False):
        if data:
            self.data = data
        self.data.update(my_instance.generate_user_data_update())
        if without_auth:
            self.response = requests.put(self.URL+self.path+self.data["id"], data=json.dumps(self.data))
        else:
            self.response = requests.put(self.URL+self.path+self.data["id"], headers=self.headers,
                                         data=json.dumps(self.data))
        self.response_json = self.response.json()
