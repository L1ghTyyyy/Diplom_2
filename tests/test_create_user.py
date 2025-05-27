import pytest
import allure
import requests
from helpers import UserData
from static_data import main_url, CREATE_USER, USER_ALREADY_EXIST


class TestCreateUser:
    @allure.title('Тест создания уникального пользователя')
    def test_create_unique_user(self, create_user):
        response = create_user
        assert response[1].json().get("success") is True
        assert response[1].status_code == 200

    @allure.title('Тест создания пользователя, который уже зарегистрирован')
    def test_create_user_already_exist(self, create_user):
        response = create_user
        payload = response[0]
        response_already_register = requests.post(main_url + CREATE_USER, data=payload)
        assert response_already_register.status_code == 403
        assert response_already_register.json().get('message') == USER_ALREADY_EXIST

    @allure.title('Тест создания пользователя и не заполнение одного из обязательных полей')
    @pytest.mark.parametrize('payload', [
        UserData.create_user_data_without_email(),
        UserData.create_user_data_without_password(),
        UserData.create_user_data_without_name()
    ])
    def test_create_user_with_no_fill_data(self, payload):
        response = requests.post(main_url + CREATE_USER, data=payload)
        assert response.status_code == 403
        assert response.json().get("success") is False