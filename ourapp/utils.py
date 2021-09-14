
import requests


def get_all_orders():
    order_payload = "https://api.quickbutik.com/v1/orders"

    headers = {
        'Authorization': 'Basic '
                         'V0MwKSlrODNOUm00ZE10KmYzI3guNHJSb1ZVaDJpI2g6V0MwKSlrODNOUm00ZE10KmYzI3guNHJSb1ZVaDJpI2g= '
    }

    all_orders = requests.get(order_payload, headers=headers)
    return all_orders.json()






