import requests
import configuration
from data import order_data
def create_order(): #Создаем заказ
    response = requests.post(f"{configuration.URL_SERVICE}{configuration.ORDERS_URL}",
                             json=order_data)
    return response.status_code, response.json()
def get_trackorder(track): #Запрашиваем инфу по трек номеру созданного заказа
    response = requests.get(f"{configuration.URL_SERVICE}{configuration.TRACK_URL}{track}")
    return response.status_code, response.json()