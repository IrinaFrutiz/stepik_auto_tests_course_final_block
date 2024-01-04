import json
import os
from dotenv import load_dotenv
import random
import allure
import requests
import pytest
from faker import Faker


load_dotenv()

URL = 'https://dummyapi.io/data/v1'
APP_ID = os.getenv('APP_ID')
fake = Faker()

headers = {
    'app-id': APP_ID,
    'Content-Type': 'application/json',
           }


@allure.feature('Check API tests')
@pytest.mark.api
class TestApi:
    @allure.title("Check create user, check userinfo, create post, delete user")
    def test_check_user_path(self):
        user_id, f_name, l_name, email = self.test_post_create_user()
        self.test_get_user_by_id(user_id, f_name, l_name, email)
        user_id, f_name, l_name, email, phone = self.test_put_update_user(user_id, email)
        self.test_get_user_by_id(user_id, f_name, l_name, email)
        post_id, img_link, likes, text, user_id = self.test_post_create_users_post(user_id)
        self.test_get_post_by_id(post_id, img_link, likes, text, user_id)
        post_id, img_link, likes, text, user_id = self.test_update_post(post_id, user_id)
        self.test_get_post_by_id(post_id, img_link, likes, text, user_id)
        delete_post(post_id)
        get_nonexistent_post(post_id)
        delete_user(user_id)
        get_nonexistent_user(user_id)

    @allure.title("Try to get user list without auth")
    def test_get_user_list_without_auth(self):
        response = requests.get(URL+'/user')
        assert response.status_code == 403, \
            f'Response: {response.status_code} is not 403'

    @allure.title("Check user list")
    def test_get_user_list(self):
        response = requests.get(URL+'/user', headers=headers)
        assert response.status_code == 200, \
            f'Response: {response.status_code} is not 200'

    @allure.title("Check user info")
    def test_get_user_by_id(self, user_id='658d761f1d2a3818e95b55fb', first_name='Laura',
                            last_name='Moran', email='thompsonnicholas@example.com'):
        response = requests.get(URL+f'/user/{user_id}', headers=headers)

        assert response.status_code == 200, \
            f'Response: {response.status_code} is not 200'
        assert response.json()['id'] == user_id, \
            f'ID in response is not equal to {user_id}'
        assert response.json()['firstName'] == first_name, \
            f'firstName in response is not equal to {first_name}'
        assert response.json()['lastName'] == last_name, \
            f'lastName in response is not equal to {last_name}'
        assert response.json()['email'] == email, \
            f'email in response is not equal to {email}'

    @allure.title("Check create user")
    def test_post_create_user(self):
        firstname, lastname = fake.name().split()
        email = fake.email()
        body = json.dumps({
            "firstName": firstname,
            "lastName": lastname,
            "email": email

        })

        response = requests.post(URL+'/user/create', headers=headers, data=body)

        assert response.status_code == 200, \
            f'Response: {response.status_code} is not 200'
        assert response.json()['firstName'] == firstname, \
            f'firstName in response is not equal to {firstname}'
        assert response.json()['lastName'] == lastname, \
            f'lastName in response is not equal to {lastname}'
        assert response.json()['email'] == email, \
            f'email in response is not equal to {email}'

        return response.json()['id'], response.json()['firstName'], \
            response.json()['lastName'], response.json()['email']

    def test_create_user_without_data(self):
        response = requests.post(URL + '/user/create', headers=headers)

        assert response.status_code == 400, \
            f'Response: {response.status_code} is not 400'
        assert response.json()['error'] == "BODY_NOT_VALID", \
            f'Wrong error'
        assert response.json()['data']['lastName'] == "Path `lastName` is required.", \
            f'Wrong lastname error in response'
        assert response.json()['data']['firstName'] == "Path `firstName` is required.", \
            f'Wrong firstName error in response'
        assert response.json()['data']['email'] == "Path `email` is required.", \
            f'Wrong email error in response'

    @allure.title("Check update user info")
    def test_put_update_user(self, user_id='659417bfa26bc4984b1f76ea', email='johnsonerica@example.com'):
        new_f_name, new_l_name = fake.name().split()
        new_phone = random.randint(1, 999999999)
        body = json.dumps({
            "firstName": new_f_name,
            "lastName": new_l_name,
            "phone": new_phone
        })

        response = requests.put(URL+f'/user/{user_id}', headers=headers, data=body)

        assert response.status_code == 200, \
            f'Response: {response.status_code} is not 200'
        assert response.json()['id'] == user_id, \
            f'user ID in response is not equal to {user_id}'
        assert response.json()['firstName'] == new_f_name, \
            f'firstName in response is not equal to {new_f_name}'
        assert response.json()['lastName'] == new_l_name, \
            f'lastName in response is not equal to {new_l_name}'
        assert response.json()['email'] == email, \
            f'email in response is not equal to {email}'
        assert response.json()['phone'] == str(new_phone), \
            f'phone in response is not equal to {new_phone}'
        return response.json()['id'], response.json()['firstName'],\
            response.json()['lastName'], response.json()['email'], \
            response.json()['phone']

    @allure.title("Check get post's list")
    def test_get_list_posts(self):
        response = requests.get(URL + f'/post', headers=headers)

        assert response.status_code == 200, \
            f'Response: {response.status_code} is not 200'

    @allure.title("Try to get post's list without auth")
    def test_get_list_posts_without_auth(self):
        response = requests.get(URL + f'/post')

        assert response.status_code == 403, \
            f'Response: {response.status_code} is not 403'

    @allure.title("Check get post list by user")
    def test_get_list_by_user(self, user_id='659417bfa26bc4984b1f76ea'):
        response = requests.get(URL+f'/user/{user_id}/post', headers=headers)

        assert response.status_code == 200, \
            f'Response: {response.status_code} is not 200'

    @allure.title("Try to get post list without auth")
    def test_get_list_by_user_without_auth(self, user_id='659417bfa26bc4984b1f76ea'):
        response = requests.get(URL+f'/user/{user_id}/post')

        assert response.status_code == 403, \
            f'Response: {response.status_code} is not 403'

    @allure.title("Check post by id")
    def test_get_post_by_id(self, post_id='65954c9b7c13cd23ea77a28f',
                            img_link='https://randomuser.me/api/portraits/women/58.jpg',
                            likes=538913, text='text', user_id='65954c9a0d9da79ce7e3b9d6'):
        response = requests.get(URL+f'/post/{post_id}', headers=headers)

        assert response.status_code == 200, \
            f'Response: {response.status_code} is not 200'
        assert response.json()['id'] == post_id, \
            f'post id in response is not {post_id}'
        assert response.json()['image'] == img_link, \
            f'image in response is not {img_link}'
        assert response.json()['likes'] == likes, \
            f'likes in response is not {likes}'
        assert response.json()['text'] == text, \
            f'text in response is not {text}'
        assert response.json()['owner']['id'] == user_id, \
            f'owner id in response is not {user_id}'

    @allure.title("Check create user's post")
    def test_post_create_users_post(self, user_id='659417bfa26bc4984b1f76ea'):
        text = random.choice(['text', 'test', 'qa', 'some text 1234567890!@#$%^&*()`~<>?:"{}'])
        img_link = "https://randomuser.me/api/portraits/women/58.jpg"
        likes = random.randint(1, 1_000_000)
        body = json.dumps({
            "text": text,
            "image": img_link,
            "likes": likes,
            "tags": "qa",
            "owner": user_id
        })
        response = requests.post(URL + f'/post/create', headers=headers, data=body)

        assert response.status_code == 200, \
            f'Response: {response.status_code} is not 200'
        assert response.json()['image'] == img_link, \
            f'image in response is not {img_link}'
        assert response.json()['likes'] == likes, \
            f'likes in response is not {likes}'
        assert response.json()['text'] == text, \
            f'text in response is not {text}'
        assert response.json()['owner']['id'] == user_id, \
            f'owner id in response is not {user_id}'
        return response.json()['id'], img_link, likes, text, user_id

    def test_create_post_without_user_id(self):
        body = json.dumps({
            "text": "text",
            "image": "img_link",
            "likes": 100
        })
        response = requests.post(URL + f'/post/create', headers=headers, data=body)

        assert response.status_code == 400, \
            f'Response: {response.status_code} is not 400'
        assert response.json()['error'] == "BODY_NOT_VALID", \
            f'Wrong error in response'

    @allure.title("Check update user's post")
    def test_update_post(self, post_id='659551257c13cd59d677a3af', user_id='659417bfa26bc4984b1f76ea'):
        text = random.choice(['text', 'test', 'qa', 'some text 1234567890!@#$%^&*()`~<>?:"{}'])
        img_link = "https://randomuser.me/api/portraits/women/58.jpg"
        likes = random.randint(1, 1_000_000)
        body = json.dumps({
            "text": text,
            "image": img_link,
            "likes": likes,
            "tags": "AA",
        })

        response = requests.put(URL + f'/post/{post_id}', headers=headers, data=body)

        assert response.status_code == 200, \
            f'Response: {response.status_code} is not 200'
        assert response.json()['image'] == img_link, \
            f'image in response is not {img_link}'
        assert response.json()['likes'] == likes, \
            f'likes in response is not {likes}'
        assert response.json()['text'] == text, \
            f'text in response is not {text}'
        assert response.json()['owner']['id'] == user_id, \
            f'owner id in response is not {user_id}'
        return response.json()['id'], img_link, likes, text, user_id

    @allure.title("Check create and after delete user")
    def test_delete_user(self):
        user_id, *_ = self.test_post_create_user()
        delete_user(user_id)

    @allure.title("Check create and after delete post")
    def test_delete_post(self):
        post_id, *_ = self.test_post_create_users_post()
        delete_post(post_id)


def delete_user(user_id):
    response = requests.delete(URL+f'/user/{user_id}', headers=headers)

    assert response.status_code == 200, \
        f'Response: {response.status_code} is not 200'
    assert response.json()['id'] == user_id, \
        f'user ID in response is not equal to {user_id}'


def get_nonexistent_user(user_id):
    response = requests.get(URL + f'/user/{user_id}', headers=headers)

    assert response.status_code == 404, \
        f'Response: {response.status_code} is not 404'
    assert response.json()['error'] == 'RESOURCE_NOT_FOUND', \
        f'Wrong error'


def delete_post(post_id):
    response = requests.delete(URL + f'/post/{post_id}', headers=headers)

    assert response.status_code == 200, \
        f'Response: {response.status_code} is not 200'
    assert response.json()['id'] == post_id, \
        f'user ID in response is not equal to {post_id}'


def get_nonexistent_post(post_id):
    response = requests.get(URL + f'/post/{post_id}', headers=headers)

    assert response.status_code == 404, \
        f'Response: {response.status_code} is not 404'
    assert response.json()['error'] == 'RESOURCE_NOT_FOUND', \
        f'Wrong error'
