import allure
import pytest
from base.test_endpoint import Endpoint


@allure.feature('Check API tests')
@pytest.mark.api
class TestApi(Endpoint):

    @allure.title("Try to get a users list without auth")
    def test_get_user_list_without_auth(self):
        self.list_all_user.new_get_list_object(True)
        self.list_all_user.check_status_code_403()

    @allure.title("Check a users list")
    def test_get_user_list(self):
        self.list_all_user.new_get_list_object()
        self.list_all_user.check_status_code_200()

    @allure.title("Check user's info")
    def test_get_user_by_id(self, data=None):
        self.get_user.new_object(data)
        self.get_user.check_status_code_200()
        self.get_user.check_id()
        self.get_user.check_first_name()
        self.get_user.check_last_name()
        self.get_user.check_email()

    @allure.title("Check create a new user")
    def test_post_create_user(self):
        self.create_user.new_object()
        self.create_user.check_status_code_200()
        self.create_user.check_first_name()
        self.create_user.check_last_name()
        self.create_user.check_email()

    @allure.title("Check errors when try to create a new user without data")
    def test_create_user_without_data(self):
        self.create_user.new_object(True)
        self.create_user.check_errors()

    @allure.title("Check create a new user without auth")
    def test_create_user_without_auth(self):
        self.create_user.new_object(True, True)
        self.create_user.check_status_code_403()

    @allure.title("Check update user's info")
    def test_put_update_user(self, data=False):
        self.update_user.new_object(data)
        self.update_user.check_status_code_200()
        self.update_user.check_first_name()
        self.update_user.check_last_name()
        self.update_user.check_email()
        self.update_user.check_phone()

    @allure.title("Check update user's info without auth")
    def test_put_update_user_without_auth(self, data=False):
        self.update_user.new_object(data, True)
        self.update_user.check_status_code_403()

    @allure.title("Check get a posts list")
    def test_get_list_posts(self):
        self.list_all_users_post.new_get_list_object()
        self.list_all_users_post.check_status_code_200()

    @allure.title("Try to get a posts list without auth")
    def test_get_list_posts_without_auth(self):
        self.list_all_users_post.new_get_list_object(True)
        self.list_all_users_post.check_status_code_403()

    @allure.title("Check get user's posts list")
    def test_get_list_by_user(self, data=False):
        self.list_users_post.new_object(data)
        self.list_users_post.check_status_code_200()

    @allure.title("Try to get user's post list without auth")
    def test_get_list_by_user_without_auth(self, data=False):
        self.list_users_post.new_object(data, True)
        self.list_users_post.check_status_code_403()

    @allure.title("Check a post by id")
    def test_get_post_by_id(self, data=False):
        self.get_users_post.new_object(data)
        self.get_users_post.check_status_code_200()
        self.get_users_post.check_id()
        self.get_users_post.check_img_link()
        self.get_users_post.check_likes()
        self.get_users_post.check_text()
        self.get_users_post.check_owner_id()

    @allure.title("Check create new user's post")
    def test_post_create_users_post(self, data=False):
        self.create_users_post.new_object(data)
        self.create_users_post.check_status_code_200()
        self.create_users_post.check_img_link()
        self.create_users_post.check_likes()
        self.create_users_post.check_text()
        self.create_users_post.check_owner_id()

    @allure.title("Check errors when try to create new user's post without user")
    def test_create_post_without_user_id(self):
        self.create_users_post.new_object({'owner': None})
        self.create_users_post.check_status_code_400()
        self.create_users_post.check_not_found_error()

    @allure.title("Check update user's post")
    def test_update_post(self, data=False):
        self.update_users_post.new_object(data)
        self.update_users_post.check_status_code_200()
        self.update_users_post.check_id()
        self.update_users_post.check_likes()
        self.update_users_post.check_img_link()
        self.update_users_post.check_text()
        self.update_users_post.check_owner_id()

    @allure.title("Check create and after delete a new user")
    def test_delete_user(self):
        self.create_user.new_object()
        self.delete_user.new_object(self.create_user.get_user_data())
        self.delete_user.check_status_code_200()
        self.delete_user.check_id()
        self.get_user.new_object(self.delete_user.get_user_data())
        self.get_user.check_status_code_404()
        self.get_user.check_not_found_error()

    @allure.title("Check create and after delete a new user without auth")
    def test_delete_user_without_auth(self):
        self.create_user.new_object()
        self.delete_user.new_object(self.create_user.get_user_data(), True)
        self.delete_user.check_status_code_403()

    @allure.title("Check create and after delete a new post")
    def test_delete_post(self):
        self.create_users_post.new_object(False)
        self.delete_users_post.new_object(self.create_users_post.get_post_data())
        self.delete_users_post.check_status_code_200()
        self.delete_users_post.check_id()
        self.get_users_post.new_object(self.delete_users_post.get_post_data())
        self.get_users_post.check_status_code_404()
        self.get_users_post.check_not_found_error()

    @allure.title("Check create and after delete a new post without auth")
    def test_delete_post_without_auth(self):
        self.create_users_post.new_object(False)
        self.delete_users_post.new_object(self.create_users_post.get_post_data(), True)
        self.delete_users_post.check_status_code_403()

    def test_two(self):
        assert 2+2 == 4, \
            f'test for check github'

# need recheck maybe change tests
#     @allure.title("Check create the user, check user's info, update the user, create user's post, check post's info,"
#                   "update the post, delete the post delete the user")
#     def test_check_users_path(self):
#         self.create_user.new_object()
#         self.create_user.check_status_code_200()
#         self.get_user.new_object(self.create_user.get_user_data())
#         self.get_user.check_status_code_200()
#         self.update_user.new_object(self.create_user.get_user_data())
#         self.update_user.check_status_code_200()
#         self.get_user.new_object(self.update_user.get_user_data())
#         self.get_user.check_status_code_200()
#         self.get_user.check_id()
#         self.get_user.check_email()
#         self.get_user.check_last_name()
#         self.get_user.check_first_name()
#         self.create_users_post.new_object(self.update_user.get_user_data()["id"])
#         self.create_users_post.check_status_code_200()
#         self.get_users_post.new_object(self.create_users_post.get_post_data())
#         self.get_users_post.check_status_code_200()
#         self.update_users_post.new_object(self.create_users_post.get_post_data())
#         self.update_users_post.check_status_code_200()
#         self.get_users_post.new_object(self.update_users_post.get_post_data())
#         self.get_users_post.check_status_code_200()
#         self.get_users_post.check_id()
#         self.get_users_post.check_text()
#         self.get_users_post.check_img_link()
#         self.get_users_post.check_likes()
#         self.get_users_post.check_owner_id()
#         self.delete_users_post.new_object(self.get_users_post.get_post_data())
#         self.delete_users_post.check_status_code_200()
#         self.delete_user.new_object(self.get_user.get_user_data())
#         self.delete_user.check_status_code_200()
