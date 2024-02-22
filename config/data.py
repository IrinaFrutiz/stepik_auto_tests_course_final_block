import json
import random
from faker import Faker


fake = Faker()


class Data:

    @classmethod
    def generate_email(cls):
        return fake.email()

    def generate_user_data(cls):
        name = fake.name()
        if len(name.split()) > 2:
            return Data.generate_user_data()
        firstname, lastname = name.split()
        email = fake.email()
        body = {
            "firstName": firstname,
            "lastName": lastname,
            "email": email
        }
        return body

    def generate_user_data_update(cls):
        name = fake.name()
        if len(name.split()) > 2:
            return Data.generate_user_data_update()
        firstname, lastname = name.split()
        new_phone = random.randint(1, 999999999)
        body = {
            "firstName": firstname,
            "lastName": lastname,
            "phone": new_phone
        }
        return body

    def generate_users_post_data(cls):
        text = random.choice(['text', 'test', 'qa', 'some text 1234567890!@#$%^&*()`~<>?:"{}'])
        likes = random.randint(1, 1_000_000)
        img_link = f"https://randomuser.me/api/portraits/women/{random.randint(1, 90)}.jpg"
        tag = random.choice(['text', 'test', 'QA', 'AA'])
        body = {
            "text": text,
            "image": img_link,
            "likes": likes,
            "tags": tag
        }
        return body
