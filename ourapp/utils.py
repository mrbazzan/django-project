
import requests


payload = "https://api.quickbutik.com/v1/"
headers = {
        'Authorization': 'Basic '
                         'V0MwKSlrODNOUm00ZE10KmYzI3guNHJSb1ZVaDJpI2g6V0MwKSlrODNOUm00ZE10KmYzI3guNHJSb1ZVaDJpI2g= '
    }


def get_all_orders():
    all_orders = requests.get(payload + 'orders', headers=headers)
    return all_orders.json()


def get_order_information():
    all_orders = get_all_orders()
    total_order = []
    for order in all_orders:
        order_information = {}
        products = []

        order_id = order['order_id']

        order_information['order_id'] = order_id

        specific_order = requests.get(payload + 'orders/?order_id={}'.format(order_id), headers=headers).json()[0]

        order_information['order_amount'] = specific_order['total_amount']
        order_information['order_date'] = specific_order['date_created'][:10]
        order_information['customer_name'] = specific_order['customer']['full_name']

        for product in specific_order['products']:
            if product['variant'] is not None:
                products.append(f"{product['title']} {product['variant']}({product['qty']})")
            else:
                products.append(f"{product['title']}({product['qty']})")

        order_information['products_sold'] = products

        total_order.append(order_information)

    return total_order
