
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.db import IntegrityError

from .models import Order
from.utils import get_all_orders


def get_orders(request):
    try:
        for order in get_all_orders():
            Order.objects.create(**order)
    except IntegrityError:
        pass

    orders = Order.objects.all()
    return render(request, 'ourapp/order.html', {'orders': orders})
