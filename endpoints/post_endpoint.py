import allure
from endpoints.base_endpoint import Base
from config.data import Data

my_instance = Data()


class Post(Base):

    @allure.title("Check a response image")
    def check_img_link(self):
        assert self.response_json['image'] == self.data["image"], \
            f'image in response is not {self.data["image"]}'

    @allure.title("Check response likes")
    def check_likes(self):
        assert self.response_json['likes'] == self.data["likes"], \
            f'image in response is not {self.data["likes"]}'

    @allure.title("Check a response text")
    def check_text(self):
        assert self.response_json['text'] == self.data["text"], \
            f'image in response is not {self.data["text"]}'

    @allure.title("Check a response owner id")
    def check_owner_id(self):
        assert self.response_json['owner']['id'] == self.data['owner'], \
            f"image in response is not {self.data['owner']}"

    def get_post_data(self):
        try:
            self.data.update({"id": self.response_json["id"]})
        except KeyError:
            self.data["id"] = self.response_json['id']
        return self.data
