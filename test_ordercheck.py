# Максимов Владимир, 9-я когорта — Финальный проект. Инженер по тестированию плюс

import data
import sender_stand_request


def positive_assert():
    new_order = sender_stand_request.create_order(data.order_data)
    track = new_order.json()["track"]
    return sender_stand_request.get_trackorder(track).status_code

#Автоматизированная проверка
def test_check_order():
    assert positive_assert() == 200

