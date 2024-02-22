import pytest

from endpoints.list_users_post import GetUsersPostList
from endpoints.list_all_users import GetAllUsersPostList
from endpoints.list_all_posts import GetAllUsersList
from endpoints.user_get import GetUser
from endpoints.user_create import CreateUser
from endpoints.user_update import UpdateUser
from endpoints.user_delete import DeleteUser
from endpoints.post_create import CreateUsersPost
from endpoints.post_get import GetUsersPost
from endpoints.post_update import UpdateUsersPost
from endpoints.post_delete import DeleteUsersPost


class Endpoint:
    list_all_user: GetAllUsersList
    list_all_users_post: GetAllUsersPostList
    list_users_post: GetUsersPostList
    create_user: CreateUser
    get_user: GetUser
    update_user: UpdateUser
    delete_user: DeleteUser
    get_users_post: GetUsersPost
    create_users_post: CreateUsersPost
    update_users_post: UpdateUsersPost
    delete_users_post: DeleteUsersPost

    @pytest.fixture(autouse=True)
    def setup(self, request, browser):
        request.cls.list_all_user = GetAllUsersList()
        request.cls.list_all_users_post = GetAllUsersPostList()
        request.cls.list_users_post = GetUsersPostList()
        request.cls.create_user = CreateUser()
        request.cls.get_user = GetUser()
        request.cls.update_user = UpdateUser()
        request.cls.delete_user = DeleteUser()
        request.cls.get_users_post = GetUsersPost()
        request.cls.create_users_post = CreateUsersPost()
        request.cls.update_users_post = UpdateUsersPost()
        request.cls.delete_users_post = DeleteUsersPost()
