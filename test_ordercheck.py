from sender_stand_request import create_order, get_trackorder

def test_get_trackorder():
    track = create_order() #Создаем заказ
    assert track is not None #Проверяем, что получен номер заказа
    status_code, _ = get_trackorder(track) #Запрашиваем инфу по созданному заказу
    assert status_code == 200