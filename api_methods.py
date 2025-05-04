import requests
import allure

from urls_for_test import TestUrls as TU

class CourierMethods:
    # Статичный метод для создания курьера
    @staticmethod
    @allure.step('Создание курьера')
    def create_courier(payload):
        response = requests.post(TU.BASE_URL + TU.CREATE_COURIER_API, data=payload)
        return response

    # Статичный метод для удаления курьера
    @staticmethod
    @allure.step('Удаление курьера')
    def delete_courier(courier_id):
        response = requests.delete(TU.BASE_URL + TU.CREATE_COURIER_API + courier_id)
        return response

    # Статичный метод для логина курьера
    @staticmethod
    @allure.step('Создание и последующая авторизация курьера')
    def courier_create_and_login_in_system(payload):
        requests.post(TU.BASE_URL + TU.CREATE_COURIER_API, data=payload)
        response = requests.post(TU.BASE_URL + TU.LOGIN_COURIER_API, data=payload)
        return response

    # Статичный метод создания двух одинаковых курьеров
    @staticmethod
    @allure.step('Создание двух одинаковых курьеров')
    def create_identical_couriers(payload):
        requests.post(TU.BASE_URL + TU.CREATE_COURIER_API, data=payload)
        response_second_courier = requests.post(TU.BASE_URL + TU.CREATE_COURIER_API, data=payload)
        return response_second_courier

    @staticmethod
    @allure.step('Авторизация курьера')
    def courier_login_in_system(payload):
        response = requests.post(TU.BASE_URL + TU.LOGIN_COURIER_API, data=payload)
        return response


class OrdersMethods:
    # Статичный метод для создания заказа
    @staticmethod
    @allure.step('Создание заказа')
    def create_order(payload):
        response = requests.post(TU.BASE_URL + TU.CREATE_AND_GET_ORDER_API, data=payload)
        return response

    # Статичный метод для получения списка всех заказов
    @staticmethod
    @allure.step('Получение списка заказов')
    def get_list_orders():
        response = requests.get(TU.BASE_URL + TU.CREATE_AND_GET_ORDER_API)
        return response