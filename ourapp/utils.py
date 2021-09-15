
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
            _product = dict()
            _product['variant'] = f"{product['variant']}"
            _product['title'] = f"{product['title']}"
            _product['qty'] = product['qty']

            if product['variant'] is not None:
                products.append(_product)
            else:
                del _product['variant']
                products.append(_product)

        order_information['products_sold'] = products

        total_order.append(order_information)

    return total_order


def customer_specific_information():
    customer_information = {}
    order_information = get_order_information()
    
    for id in order_information:
        customer_name = id['customer_name']
        if customer_name not in customer_information:
            customer_information[customer_name] = {'order_amount': 0, 'order_date': '', 'products_sold': {}}

        customer_information[customer_name]['order_amount'] += float(id['order_amount'])
        customer_information[customer_name]['order_date']= id['order_date']

        _product = {}
        for product in id['products_sold']:
            if product['title'] not in _product:
                _product[product['title']] = 0

            if product['title'] in _product:
                _product[product['title']] += int(product['qty'])
        
        for article, qty in _product.items():
            if article not in customer_information[customer_name]['products_sold']:
                customer_information[customer_name]['products_sold'][article] = qty

            customer_information[customer_name]['products_sold'][article] += qty

    return customer_information


def most_sold_article(customer_information):
    items = {}
    for order in customer_information:
        for item, qty in customer_information[order]['products_sold'].items():
            if item in items:
                items[item] += qty
            else:
                items[item] = qty

    return sorted(items, key=lambda x: items[x], reverse=True)
