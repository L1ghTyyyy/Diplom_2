import pytest
import requests
from helpers import UserData
from static_data import main_url, CREATE_USER, DELETE_USER


@pytest.fixture
def create_user():  #создание пользователя
    payload = UserData.create_user_data()
    response = requests.post(main_url + CREATE_USER, data=payload)
    yield payload, response
    token = response.json()['accessToken']
    requests.delete(main_url + DELETE_USER, headers={"Authorization": token})