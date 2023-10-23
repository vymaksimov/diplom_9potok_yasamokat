import requests
import configuration
import data


#Создаем заказ
def create_order(order_data):
    return requests.post(configuration.URL_SERVICE + configuration.ORDERS_URL,
                             json=order_data)

#Запрашиваем инфу по трек номеру созданного заказа
def get_trackorder(track):
    return requests.get(configuration.URL_SERVICE + configuration.TRACK_URL + str(track))

