import pytest
import requests

from urls_for_test import TestUrls as TU
from helper import DataForCreateCourier as DFCC


@pytest.fixture(scope='function')
def create_and_delete_courier():
    """
        Создает курьера перед тестом и удаляет его после завершения теста.
    """
    payload = DFCC.generate_fake_data_for_create_courier()
    yield payload
    login = requests.post(TU.BASE_URL + TU.LOGIN_COURIER_API, data=payload)
    id_courier = login.json()['id']
    requests.delete(TU.BASE_URL + TU.CREATE_COURIER_API + str(id_courier))