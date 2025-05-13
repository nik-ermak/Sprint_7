import pytest
import allure

from helper import DataForMakeOrder as DFMO
from api_methods import OrdersMethods as OM

class TestCreateOrder:
    # Создание заказа с чёрным и серым цветом
    @allure.title('Создание заказа с использованием одного цвета')
    @pytest.mark.parametrize('color', [['BLACK'], ['GREY']])
    def test_make_order_with_color(self, color):
        data_for_order = DFMO.generate_fake_data_for_make_order(color)
        response = OM.create_order(data_for_order)
        assert response.status_code == 201 and 'track' in response.text

    # Создание заказа одновременно с использованием 2х цветов
    @allure.title('Создание заказа с использованием 2х цветов')
    @pytest.mark.parametrize('color', ['BLACK', 'GREY'])
    def test_make_order_with_two_color(self, color):
        data_for_order = DFMO.generate_fake_data_for_make_order(color)
        response = OM.create_order(data_for_order)
        assert response.status_code == 201 and 'track' in response.text

    # Создание заказа без использования цвета
    @allure.title('Создания заказа без использования цвета самоката')
    def test_make_order_without_color(self):
        data_for_order = DFMO.generate_fake_data_for_make_order('')
        response = OM.create_order(data_for_order)
        assert response.status_code == 201 and 'track' in response.text