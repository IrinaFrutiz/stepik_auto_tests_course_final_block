from faker import Faker


class Data:
    fake = Faker()
    email = fake.name() + fake.email()
