import requests
import allure
from static_data import main_url, CREATE_ORDER, GET_ORDERS, NOT_AUTHORISED, Ingredients


class TestGetOrder:
    @allure.title('Тест получения заказов авторизованного пользователя')
    def test_get_orders_by_authorized_user(self, create_user):
        token = create_user[1].json()['accessToken']
        headers = {'Authorization': token}
        response_create_order = requests.post(main_url + CREATE_ORDER, headers=headers, data=Ingredients.correct_ingredients_hash_data)
        response_get_order = requests.get(main_url + GET_ORDERS, headers=headers)

        assert response_get_order.status_code == 200
        assert response_create_order.json()['order']['number'] == response_get_order.json()['orders'][0]['number']

    @allure.title('Тест получения заказов неавторизованного пользователя')
    def test_get_orders_by_unauthorized_user(self):
        response_get_orders = requests.get(main_url + GET_ORDERS)

        assert response_get_orders.status_code == 401
        assert NOT_AUTHORISED in response_get_orders.text