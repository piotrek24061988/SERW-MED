from django.shortcuts import render
from .models import *


class SerwMedStore:
    def __init__(self):
        pass

    @staticmethod
    def store(request):
        context = {'products': Product.objects.all()}
        return render(request, 'store.html', context)

    @staticmethod
    def cart(request):
        if request.user.is_authenticated:
            if request.user.customer:
                customer = request.user.customer
                order, created = Order.objects.get_or_create(customer=customer, complete=False)
                items = order.orderitem_set.all()
            else:
                items = []
                order = {'get_cart_total': 0, 'get_cart_items': 0}
        else:
            items = []
            order = {'get_cart_total': 0, 'get_cart_items': 0}
        context = {'items': items, 'order': order}
        return render(request, 'cart.html', context)

    @staticmethod
    def checkout(request):
        if request.user.is_authenticated:
            if request.user.customer:
                customer = request.user.customer
                order, created = Order.objects.get_or_create(customer=customer, complete=False)
                items = order.orderitem_set.all()
            else:
                items = []
                order = {'get_cart_total': 0, 'get_cart_items': 0}
        else:
            items = []
            order = {'get_cart_total': 0, 'get_cart_items': 0}
        context = {'items': items, 'order': order}
        return render(request, 'checkout.html', context)

