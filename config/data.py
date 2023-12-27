from faker import Faker


class Data:
    @classmethod
    def generate_email(cls):
        fake = Faker()
        return fake.email()
