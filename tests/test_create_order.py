import requests
import allure
from static_data import main_url, CREATE_ORDER, INTERNAL_SERVER_ERROR, Ingredients



class TestCreateOrder:

    @allure.title('Тест создания заказа с авторизацией пользователя')
    def test_create_order_with_authorized_user(self, create_user):
        token = create_user[1].json()['accessToken']
        headers = {'Authorization': token}
        response = requests.post(main_url + CREATE_ORDER, headers=headers, data=Ingredients.correct_ingredients_hash_data)
        assert response.status_code == 200
        assert response.json().get('success') is True

    @allure.title('Тест создания заказа без авторизации пользователя')
    def test_create_order_by_unauthorized_user(self):
        response = requests.post(main_url + CREATE_ORDER, data=Ingredients.correct_ingredients_hash_data)
        assert response.status_code == 200
        assert response.json().get('success') is True

    @allure.title('Тест создания заказа с неверным хешем ингредиентов')
    def test_create_order_with_invalid_hash(self, create_user):
        token = create_user[1].json()['accessToken']
        headers = {'Authorization': token}
        response = requests.post(main_url + CREATE_ORDER, headers=headers, data=Ingredients.incorrect_ingredients_hash_data)
        assert response.status_code == 500
        assert INTERNAL_SERVER_ERROR in response.text

    @allure.title('Тест создания заказа с ингредиентами')
    def test_create_order_with_ingredients(self, create_user):
        token = create_user[1].json()['accessToken']
        headers = {'Authorization': token}
        response = requests.post(main_url + CREATE_ORDER, headers=headers, data=Ingredients.correct_ingredients_hash_data)
        assert response.status_code == 200
        assert response.json().get('success') is True

    @allure.title('Тест создания заказа без ингредиентов')
    def test_create_order_without_ingredients(self, create_user):
        token = create_user[1].json()['accessToken']
        headers = {'Authorization': token}
        response = requests.post(main_url + CREATE_ORDER, headers=headers, data=Ingredients.empty_ingredients_data)
        assert response.status_code == 400
        assert response.json().get('success') is False