import json
import random

from faker import Faker
from datetime import date

class DataForCreateCourier:
    # Метод для генерации данных для создания/регистрации курьера
    @staticmethod
    def generate_fake_data_for_create_courier():
        fake = Faker()
        login = f'{fake.user_name()}{fake.random_number(digits=5)}'
        password = fake.password(length=12)
        first_name = fake.first_name()
        payload = {
            'login': login,
            'password': password,
            'first_name': first_name
        }
        return payload


class DataForMakeOrder:
    # Метод для генерации данных для заказа самоката, на вход подаём цвет самоката
    @staticmethod
    def generate_fake_data_for_make_order(color_scooter):
        fake = Faker(locale="ru_RU")
        payload = {
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "address": fake.address(),
            "metroStation": random.randrange(5),
            "phone": fake.phone_number(),
            "rentTime": random.randrange(5),
            "deliveryDate": fake.date_between(start_date='today', end_date='+30d'),
            "comment": fake.text(max_nb_chars=15),
            "color": color_scooter
        }
        return json.dumps(payload, default=lambda o: o.isoformat() if isinstance(o, date) else str(o))
