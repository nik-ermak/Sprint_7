import pytest
import allure

from api_methods import CourierMethods as CM
from helper import DataForCreateCourier as DFCC
from conftest import create_and_delete_courier

class TestCreateCourier:
    # Создание курьера. Валидные данные
    @allure.title('Создание курьера')
    def test_create_courier_success(self, create_and_delete_courier):
        response = CM.create_courier(create_and_delete_courier)
        assert response.status_code == 201 and response.text == '{"ok":true}'

    # Создание двух идентичных курьеров. Валидные данные
    @allure.title('Создание двух идентичных курьеров')
    def test_create_two_identical_courier(self, create_and_delete_courier):
        response = CM.create_identical_couriers(create_and_delete_courier)
        assert response.status_code == 409 and response.json()['message'] == 'Этот логин уже используется. Попробуйте другой.'

    # Создание курьера. Неполные данные
    @allure.title('Создания курьера с неполным набором данных')
    @pytest.mark.parametrize('data', ['login', 'password'])
    def test_crate_courier_without_required_data(self, data):
        payload = DFCC.generate_fake_data_for_create_courier()
        payload.pop(data)
        response = CM.create_courier(payload)
        assert response.status_code == 400 and response.json()['message'] == 'Недостаточно данных для создания учетной записи'