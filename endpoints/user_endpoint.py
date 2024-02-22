import allure
from endpoints.base_endpoint import Base
from config.data import Data


my_instance = Data()


class User(Base):

    @allure.title("Check an expected first name and a first name in response")
    def check_first_name(self):
        assert self.response_json['firstName'] == self.data["firstName"], \
            f'firstName in response is not equal to {self.data["firstName"]}'

    @allure.title("Check an expected last name and a last name in response")
    def check_last_name(self):
        assert self.response_json['lastName'] == self.data["lastName"], \
            f'lastName in response is not equal to {self.data["lastName"]}'

    @allure.title("Check an expected email and an email in response")
    def check_email(self):
        assert self.response_json['email'] == self.data["email"], \
            f'email in response is not equal to {self.data["email"]}'

    @allure.title("Check a phone in response")
    def check_phone(self):
        assert self.response_json['phone'] == str(self.data["phone"]), \
            f'phone in response is not equal to {self.data["phone"]}'

    def get_user_data(self):
        try:
            self.data.update({"id": self.response_json["id"]})
        except KeyError:
            self.data["id"] = self.response_json["id"]
        return self.data
