from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import *


class SerwMedStore:
    def __init__(self):
        pass

    @staticmethod
    def store(request):
        if request.user.is_authenticated:
            if request.user.customer: #hasattr(request.user, 'customers') and
                customer = request.user.customer
                order, created = Order.objects.get_or_create(customer=customer, complete=False)
                items = order.orderitem_set.all()
                cartItems = order.get_cart_items
            else:
                items = []
                order = {'get_cart_total': 0, 'get_cart_items': 0}
                cartItems = order['get_cart_items']
        else:
            items = []
            order = {'get_cart_total': 0, 'get_cart_items': 0}
            cartItems = order['get_cart_items']

        context = {'products': Product.objects.all(), 'cartItems': cartItems}
        return render(request, 'store.html', context)

    @staticmethod
    def cart(request):
        if request.user.is_authenticated:
            if request.user.customer: #hasattr(request.user, 'customers') and
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
            if request.user.customer: #hasattr(request.user, 'customers') and
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

    @staticmethod
    def updateItem(request):
        data = json.loads(request.body)
        productId = data['productId']
        action = data['action']
        print('Action', action)
        print('productId', productId)

        customer = request.user.customer
        product = Product.objects.get(id=productId)

        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

        if action == 'add':
            orderItem.quantity = (orderItem.quantity+1)
        elif action == 'remove':
            orderItem.quantity = (orderItem.quantity-1)

        orderItem.save()

        if orderItem.quantity <= 0:
            orderItem.delete()

        return JsonResponse('Item was added', safe=False)

