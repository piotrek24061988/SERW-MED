from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core.mail import send_mail
from django.contrib import messages
import json
import datetime
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
                order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
                cartItems = order['get_cart_items']
        else:
            items = []
            order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
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
                order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        else:
            items = []
            order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
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
                order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        else:
            items = []
            order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        context = {'items': items, 'order': order}
        return render(request, 'checkout.html', context)

    @staticmethod
    def updateItem(request):
        data = json.loads(request.body)
        productId = data['productId']
        action = data['action']

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

    @staticmethod
    def processOrder(request):
        transaction_id = datetime.datetime.now().timestamp()
        data = json.loads(request.body)

        if request.user.is_authenticated:
            customer = request.user.customer
            order, created = Order.objects.get_or_create(customer=customer, complete=False)
            total = float(data['userFormData']['total'])
            order.transaction_id = transaction_id
            order.payment = data['userFormData']['payment']

            if total == order.get_cart_total:
                order.complete = True
            order.save()

            items = order.orderitem_set.all()
            itemsStr = ''
            for item in items:
                itemsStr = itemsStr + 'produkt: ' + str(item.product.name) + ', ilość: ' + str(item.quantity) + ', cena łączna: ' + str(item.get_total) + ', '

            if order.shipping:
                ShippingAddress.objects.create(
                    customer=customer,
                    order=order,
                    address=data['userShippingInfo']['adres'],
                    city=data['userShippingInfo']['miasto'],
                    zipcode=data['userShippingInfo']['kod'],
                    number=data['userShippingInfo']['telefon']
                )

            if order.complete:
                send_mail("Django Order - name:  " + customer.name + ", email: " + customer.email + ", tytuł: złożone zamówienie",
                          "total: " + str(total) + ", transaction_id: " + str(transaction_id) + ", payment: " + order.payment +
                          ", address: " + str(data['userShippingInfo']['adres']) + ", miasto: " + str(data['userShippingInfo']['miasto']) +
                          ", kod: " + str(data['userShippingInfo']['kod']) + ", telefon: " + str(data['userShippingInfo']['telefon']) +
                          ", lista produktów: " + itemsStr,
                          'piotrek24061988@gmail.com',
                          ['piotrek24061988@gmail.com', 'wieslawagorecka1953@gmail.com', customer.email], fail_silently=True)
                messages.success(request, 'Twoje zamówienie zostało złożone')
        else:
            print('User is not logged in')
        return JsonResponse('Payment complete', safe=False)
