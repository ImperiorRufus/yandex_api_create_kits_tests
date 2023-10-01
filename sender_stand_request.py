import configuration
import requests
import data


def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)
#Функция для создания нового пользователя, с целью получить токен авторизации


def post_new_kit(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_NEW_KIT_PATH,
                         json=body,
                         headers=data.kit_headers)
#Функция для создания нового набора
