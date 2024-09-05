from faker import Faker


def get_fake_email() -> str:
    fake_email = Faker().email(domain='yandex.ru')
    return fake_email
