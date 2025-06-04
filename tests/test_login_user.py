import allure
import requests
from helpers import UserData
from static_data import main_url, LOGIN


class TestLoginUser:
    @allure.title('Тест логина под существующим пользователем')
    def test_user_login(self, create_user):
        response = create_user
        login = requests.post(main_url + LOGIN, data=response[0])
        assert login.status_code == 200
        assert login.json().get("success") is True

    @allure.title('Тест логина с неверным логином и паролем')
    def test_login_nonexistent_user(self):
        login_request = requests.post(main_url + LOGIN, data=UserData.create_user_data_without_name())
        assert login_request.status_code == 401
        assert login_request.json().get("success") is False