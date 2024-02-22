import os
from dotenv import load_dotenv
import allure


load_dotenv()


class Base:
    response = None
    response_json = None
    data = {}
    URL = 'https://dummyapi.io/data/v1'
    path = ""
    headers = {
        'app-id': os.getenv('APP_ID'),
        'Content-Type': 'application/json',
    }

    @allure.title("Check status code in response = 200")
    def check_status_code_200(self):
        assert self.response.status_code == 200, \
            f'Response: {self.response.status_code} is not 200'

    @allure.title("Check a response status code is 400")
    def check_status_code_400(self):
        assert self.response.status_code == 400, \
            f'Response: {self.response.status_code} is not 400'

    @allure.title("Check status code in response = 403")
    def check_status_code_403(self):
        assert self.response.status_code == 403, \
            f'Response: {self.response.status_code} is not 403'

    @allure.title("Check status code in response = 404")
    def check_status_code_404(self):
        assert self.response.status_code == 404, \
            f'Response: {self.response.status_code} is not 404'

    @allure.title("Check a response id")
    def check_id(self):
        assert self.response_json['id'] == self.data["id"], \
            f'ID in response is not equal to {self.data["id"]}'
