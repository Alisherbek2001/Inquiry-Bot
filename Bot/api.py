import requests
import os


BASE_URL = os.getenv("BASE_URL")


def create_user(telegram_id,language):
    response = requests.post(f"{BASE_URL}",
                             data={'telegram_id': telegram_id, 'language': language})
    return response.status_code


def check_user(telegram_id):
    response = requests.get(f"{BASE_URL}{telegram_id}")
    return response

def change_language(telegram_id,language):
    response = requests.put(f"{BASE_URL}{telegram_id}/",
                            data={"language":language})
    return response


# print(change_language(994276762,'ru').status_code)

