main_url = 'https://stellarburgers.nomoreparties.site'  #главный URL

CREATE_USER = '/api/auth/register'  #создание пользователя
DELETE_USER = '/api/auth/user'  #удаление пользователя
LOGIN = '/api/auth/login'  #логин пользователя
CREATE_ORDER = '/api/orders'  #создание заказа
GET_ORDERS = '/api/orders'  #получение заказа
CHANGE_DATA = '/api/auth/user'  #изменение данных пользователя
class Ingredients:
    correct_ingredients_hash_data = {  #корректные хеши ингредиентов
        "ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f"]
        }
    incorrect_ingredients_hash_data = {  #некорректные хеши ингредиентов
        "ingredients": ["69d5b44abracadabaraf6a76", "609646e4daboradabara2870"]
        }
    empty_ingredients_data = {  #без ингредиентов
        "ingredients": []
        }

USER_ALREADY_EXIST = 'User already exists'
INTERNAL_SERVER_ERROR = 'Internal Server Error'
NOT_AUTHORISED = 'You should be authorised'