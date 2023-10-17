import config
import body
import requests


# Функция создания нового заказа
def create_new_order(order_body):
    return requests.post(config.URL_SERVICE + config.CREATE_ORDER_PATH, json=order_body)


response = create_new_order(body.order_body)
print(response.status_code)
print(response.json())


# Функция сохранения номера трека заказа
def save_number_of_order():
    actual_number = response
    return actual_number.json()["track"]


print(save_number_of_order())


# Функция получения заказа по номеру заказа созданному ранее
def get_order_using_actual_number():
    return requests.get(config.URL_SERVICE + config.GET_ORDER_BY_NUM + f"?t={save_number_of_order()}")


get_answer = get_order_using_actual_number()
print(get_answer.status_code)
print(get_answer.json())


def test_get_by_number_positive():
    assert get_answer.status_code == 200


# Дмитрий Варлыга, 9-я когорта — Финальный проект. Инженер по тестированию плюс
