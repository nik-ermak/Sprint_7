import allure

from api_methods import OrdersMethods as OM

class TestGetOrderList:
    @allure.title('получение списка заказов')
    def test_get_order_list(self):
        response = OM.get_list_orders()
        assert response.status_code == 200 and 'track' in response.json()['orders'][0]
