import json
import random

import requests
import pytest
from faker import Faker


URL = 'https://dummyapi.io/data/v1'
APP_ID = '658d653cd8814e0193b7d0aa'
fake = Faker()

headers = {
    'app-id': APP_ID,
    'Content-Type': 'application/json',
           }


@pytest.mark.api
class TestApi:
    def test_get_user_list_without_auth(self):
        response = requests.get(URL+'/user')
        assert response.status_code == 403, \
            f'Response: {response.status_code} is not 403'

    def test_get_user_list(self):
        response = requests.get(URL+'/user', headers=headers)
        assert response.status_code == 200, \
            f'Response: {response.status_code} is not 200'

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

    def test_check_all_user_path(self):
        user_id, f_name, l_name, email = self.test_post_create_user()
        self.test_get_user_by_id(user_id, f_name, l_name, email)
        user_id, f_name, l_name, email, phone = self.test_put_update_user(user_id, email)
        self.test_get_user_by_id(user_id, f_name, l_name, email)
        self.delete_user(user_id)
        self.get_nonexistent_user(user_id)

    def test_get_list_posts(self):
        response = requests.get(URL + f'/post', headers=headers)

        assert response.status_code == 200, \
            f'Response: {response.status_code} is not 200'

    def test_get_list_by_user(self, user_id='659417bfa26bc4984b1f76ea'):
        response = requests.get(URL+f'/user/{user_id}/post', headers=headers)

        assert response.status_code == 200, \
            f'Response: {response.status_code} is not 200'

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
        print(response.json())
        return response.json()['id']
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
