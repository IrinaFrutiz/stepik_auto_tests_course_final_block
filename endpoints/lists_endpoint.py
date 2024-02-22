import requests
from endpoints.base_endpoint import Base


class List(Base):
    def new_get_list_object(self, without=False):
        if without:
            self.response = requests.get(self.URL+self.path)
        else:
            self.response = requests.get(self.URL+self.path, headers=self.headers)
        self.response_json = self.response.json()
