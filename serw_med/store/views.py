from django.shortcuts import render
from django.http import JsonResponse
from django.core.mail import send_mail
from django.contrib import messages
import json
import datetime
from .models import *
from news.models import Emails


class SerwMedStore:
    def __init__(self):
        pass

    @staticmethod
    def store(request):
        if request.user.is_authenticated:
            order, created = Order.objects.get_or_create(customer=request.user, complete=False)
            cartItems = order.get_cart_items
        else:
            order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
            cartItems = order['get_cart_items']

            try:
                cart = json.loads(request.COOKIES['cart'])
            except:
                cart = {}

            for i in cart:
                try:
                    cartItems += cart[i]["quantity"]
                except:
                    pass

        context = {'products': Product.objects.all(), 'cartItems': cartItems}
        return render(request, 'store.html', context)

    @staticmethod
    def cart(request):
        if request.user.is_authenticated:
            order, created = Order.objects.get_or_create(customer=request.user, complete=False)
            items = order.orderitem_set.all()
        else:
            items = []
            order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}

            try:
                cart = json.loads(request.COOKIES['cart'])
            except:
                cart = {}

            for i in cart:
                try:
                    product = Product.objects.get(id=i)
                    total = (product.price * cart[i]["quantity"])
                    order['get_cart_total'] += total
                    order['get_cart_items'] += cart[i]["quantity"]

                    item = {
                        'product': {
                            'id': product.id,
                            'name': product.name,
                            'price': product.price,
                            'imageURL': product.imageURL
                        },
                        'quantity': cart[i]["quantity"],
                        'get_total': total
                    }
                    items.append(item)

                    if not product.digital:
                        order['shipping'] = True
                except:
                    pass

        context = {'items': items, 'order': order}
        return render(request, 'cart.html', context)

    @staticmethod
    def checkout(request):
        if request.user.is_authenticated:
            customer = request.user
            order, created = Order.objects.get_or_create(customer=customer, complete=False)
            items = order.orderitem_set.all()
        else:
            items = []
            order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}

            try:
                cart = json.loads(request.COOKIES['cart'])
            except:
                cart = {}

            for i in cart:
                try:
                    product = Product.objects.get(id=i)
                    total = (product.price * cart[i]["quantity"])
                    order['get_cart_total'] += total
                    order['get_cart_items'] += cart[i]["quantity"]

                    item = {
                        'product': {
                            'id': product.id,
                            'name': product.name,
                            'price': product.price,
                            'imageURL': product.imageURL
                        },
                        'quantity': cart[i]["quantity"],
                        'get_total': total
                    }
                    items.append(item)

                    if not product.digital:
                        order['shipping'] = True
                except:
                    pass

        context = {'items': items, 'order': order}
        return render(request, 'checkout.html', context)

    @staticmethod
    def updateItem(request):
        if request.user.is_authenticated:
            data = json.loads(request.body)
            productId = data['productId']
            action = data['action']

            customer = request.user
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

            return JsonResponse('Item added', safe=False)
        else:
            return JsonResponse('User unauthenticated', safe=False)

    @staticmethod
    def processOrder(request):
        transaction_id = datetime.datetime.now().timestamp()
        data = json.loads(request.body)

        if request.user.is_authenticated:
            customer = request.user
            order, created = Order.objects.get_or_create(customer=customer, complete=False)
            total = float(data['userFormData']['total'])
            order.transaction_id = transaction_id
            order.payment = data['userFormData']['payment']

            if total == order.get_cart_total:
                order.complete = True
            order.save()

            if order.shipping:
                ShippingAddress.objects.create(
                    customer=customer,
                    order=order,
                    address=data['userShippingInfo']['adres'],
                    city=data['userShippingInfo']['miasto'],
                    zipcode=data['userShippingInfo']['kod'],
                    number=data['userShippingInfo']['telefon']
                )

            # sending email on successful order
            if order.complete:
                items = order.orderitem_set.all()
                itemsStr = ''
                for item in items:
                    itemsStr = itemsStr + 'produkt: ' + str(item.product.name) + ', ilość: ' + str(
                        item.quantity) + ', cena łączna: ' + str(item.get_total) + ', '

                emailTitle = "Django Order - name:  " + customer.username + ", email: " + customer.email + ", tytuł: złożone zamówienie"
                emailContent = "total: " + str(total) + ", transaction_id: " + str(transaction_id) + ", payment: " + order.payment + \
                          ", adres: " + str(data['userShippingInfo']['adres']) + ", miasto: " + str(data['userShippingInfo']['miasto']) + \
                          ", kod: " + str(data['userShippingInfo']['kod']) + ", telefon: " + str(data['userShippingInfo']['telefon']) + \
                          ", lista produktów: " + itemsStr
                send_mail(emailTitle, emailContent, 'piotrek24061988@gmail.com',
                          ['piotrek24061988@gmail.com', 'wieslawagorecka1953@gmail.com', customer.email], fail_silently=True)
                emails = Emails(name=customer.username, email=customer.email, title=emailTitle, content=emailContent)
                emails.save()
                messages.success(request, 'Twoje zamówienie zostało złożone')

                return JsonResponse('Payment completed', safe=False)
            else:
                return JsonResponse('Payment didnt complete', safe=False)
        else:
            print(1)
            print(data['userFormData'])
            #print(data['userFormData']['name'])
            print(data['userFormData']['email'])
            #customer, created = User.objects.get_or_create(username="Incognito", email="Incognito@com.pl")#email=data['userFormData']['email']
            #customer, created = User.objects.get_or_create(email=data['userFormData']['email'])
            if not User.objects.filter(username=data['userFormData']['name'], email=data['userFormData']['email']).exists():
                customer = User.objects.create_user(username=data['userFormData']['name'], email=data['userFormData']['email'])
            else:
                customer = User.objects.get(username=data['userFormData']['name'], email=data['userFormData']['email'])
            print(2)
            customer.save()
            print(3)

            orderStub = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
            order = Order.objects.create(customer=customer, complete=False)
            items = []

            try:
                cart = json.loads(request.COOKIES['cart'])
            except:
                cart = {}

            for i in cart:
                try:
                    product = Product.objects.get(id=i)
                    total = (product.price * cart[i]["quantity"])
                    orderStub['get_cart_total'] += total
                    orderStub['get_cart_items'] += cart[i]["quantity"]

                    item = {
                        'product': {
                            'id': product.id,
                            'name': product.name,
                            'price': product.price,
                            'imageURL': product.imageURL
                        },
                        'quantity': cart[i]["quantity"],
                        'get_total': total
                    }
                    items.append(item)
                    orderItem = OrderItem.objects.create(product=product, order=order, quantity=cart[i]["quantity"])

                    if not product.digital:
                        orderStub['shipping'] = True

                except:
                    pass

            total = float(data['userFormData']['total'])
            order.transaction_id = transaction_id
            order.payment = data['userFormData']['payment']

            print("total:", total)
            print("orderStub.get_cart_total:", orderStub['get_cart_total'])
            print("order.get_cart_total:", order.get_cart_total)
            if total == order.get_cart_total:
                order.complete = True
            order.save()

            print("order.shipping:", order.shipping)
            print("orderStub.shipping:", orderStub['shipping'])
            if order.shipping:
                ShippingAddress.objects.create(
                    customer=customer,
                    order=order,
                    address=data['userShippingInfo']['adres'],
                    city=data['userShippingInfo']['miasto'],
                    zipcode=data['userShippingInfo']['kod'],
                    number=data['userShippingInfo']['telefon']
                )

            # sending email on successful order
            if order.complete:
                items = order.orderitem_set.all()
                itemsStr = ''
                for item in items:
                    itemsStr = itemsStr + 'produkt: ' + str(item.product.name) + ', ilość: ' + str(
                        item.quantity) + ', cena łączna: ' + str(item.get_total) + ', '

                emailTitle = "Django Order - name:  " + customer.username + ", email: " + customer.email + ", tytuł: złożone zamówienie"
                emailContent = "total: " + str(total) + ", transaction_id: " + str(transaction_id) + ", payment: " + order.payment + \
                          ", adres: " + str(data['userShippingInfo']['adres']) + ", miasto: " + str(data['userShippingInfo']['miasto']) + \
                          ", kod: " + str(data['userShippingInfo']['kod']) + ", telefon: " + str(data['userShippingInfo']['telefon']) + \
                          ", lista produktów: " + itemsStr
                send_mail(emailTitle, emailContent, 'piotrek24061988@gmail.com',
                          ['piotrek24061988@gmail.com', 'wieslawagorecka1953@gmail.com', customer.email], fail_silently=True)
                emails = Emails(name=customer.username, email=customer.email, title=emailTitle, content=emailContent)
                emails.save()
                messages.success(request, 'Twoje zamówienie zostało złożone')

                return JsonResponse('Payment completed', safe=False)
            else:
                return JsonResponse('Payment didnt complete', safe=False)
