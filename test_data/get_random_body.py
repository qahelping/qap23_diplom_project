from faker import Faker


def get_random_user():
    fake = Faker()
    return {
        "name": fake.name(),
        "email": fake.email(),
        "gender": "male" if fake.passport_gender() == "M" else "female",
        "status": "active",
    }
