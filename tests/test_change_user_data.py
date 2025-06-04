import pytest
import requests
import allure
from static_data import main_url, CHANGE_DATA, NOT_AUTHORISED
from helpers import UserData


class TestChangeUserData:

    @allure.title('Тест изменения данных с авторизацией')
    @pytest.mark.parametrize('data', [
        UserData.create_user_data()['name'],
        UserData.create_user_data()['email'],
        UserData.create_user_data()['password']
    ])
    def test_change_user_data(self, create_user, data):
        token = create_user[1].json()['accessToken']
        headers = {'Authorization': token}
        response = requests.patch(main_url + CHANGE_DATA, headers=headers, data=data)
        assert response.status_code == 200
        assert response.json().get('success') is True

    @allure.title('Тест изменения данных без авторизации')
    @pytest.mark.parametrize('data', [
        UserData.create_user_data()['name'],
        UserData.create_user_data()['email'],
        UserData.create_user_data()['password']
    ])
    def test_change_unauthorized_user_data(self, data):
        response = requests.patch(main_url + CHANGE_DATA, data=data)
        assert response.status_code == 401
        assert response.json().get('message') == NOT_AUTHORISED