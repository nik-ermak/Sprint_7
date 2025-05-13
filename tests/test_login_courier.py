import pytest
import allure

from api_methods import CourierMethods as CM
from helper import DataForCreateCourier as DFCC
from conftest import create_and_delete_courier

class TestCourierLogin:

    # Авторизация курьера
    @allure.title('Авторизация курьера')
    def test_courier_login_success(self, create_and_delete_courier):
        response = CM.courier_create_and_login_in_system(create_and_delete_courier)
        assert response.status_code == 200 and 'id' in response.json()

    # Авторизация курьера с неполными данными
    @allure.title('Авторизация курьера с неполным набором данных')
    @pytest.mark.parametrize('data, value', [('login', ''), ('password', '')])
    def test_courier_login_without_data(self, data, value):
        payload = DFCC.generate_fake_data_for_create_courier()
        payload[data] = value
        response = CM.courier_create_and_login_in_system(payload)
        assert response.status_code == 400 and response.json()['message'] == 'Недостаточно данных для входа'

    @allure.title('Авторизация несуществующего курьера')
    def test_courier_login_with_random_data(self):
        payload = DFCC.generate_fake_data_for_create_courier()
        response = CM.courier_login_in_system(payload)
        assert response.status_code == 404 and response.json()['message'] == 'Учетная запись не найдена'


