from django.shortcuts import render
from django.http import JsonResponse
from django.core.mail import send_mail
from django.contrib import messages
from django.views.generic import DetailView
import json
import datetime
from .models import *
from news.models import Emails


class SerwMedStoreProduct(DetailView):
    model = Product
    template_name = 'product_single.html'


class SerwMedStore:
    def __init__(self):
        pass

    @staticmethod
    def processCookies(request, items, order, createOrderItem):
        try:
            cart = json.loads(request.COOKIES['cart'])

            for i in cart:
                product = Product.objects.get(id=i)
                total = (product.price * cart[i]["quantity"])
                if not createOrderItem:
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
                if createOrderItem:
                    OrderItem.objects.create(product=product, order=order, quantity=cart[i]["quantity"])

                if not product.digital and not createOrderItem:
                    order['shipping'] = True
        except:
            pass

    @staticmethod
    def prepareContext(request):
        if request.user.is_authenticated:
            order, created = Order.objects.get_or_create(customer=request.user, complete=False)
            items = order.orderitem_set.all()
            cartItems = order.get_cart_items
        else:
            items = []
            order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}

        SerwMedStore.processCookies(request, items, order, False)

        if not request.user.is_authenticated:
            cartItems = order['get_cart_items']

        return {'items': items, 'order': order, 'products': Product.objects.all(), 'cartItems': cartItems}

    @staticmethod
    def store(request):
        return render(request, 'store.html', SerwMedStore.prepareContext(request))

    @staticmethod
    def cart(request):
        return render(request, 'cart.html', SerwMedStore.prepareContext(request))

    @staticmethod
    def checkout(request):
        return render(request, 'checkout.html', SerwMedStore.prepareContext(request))

    @staticmethod
    def updateItem(request):
        if request.user.is_authenticated:
            data = json.loads(request.body)
            productId = data['productId']
            action = data['action']

            product = Product.objects.get(id=productId)

            order, created = Order.objects.get_or_create(customer=request.user, complete=False)
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
            order, created = Order.objects.get_or_create(customer=request.user, complete=False)
        else:
            newUserName = data['userFormData']['name']
            newUserEmail = data['userFormData']['email']
            if not User.objects.filter(username=newUserName, email=newUserEmail).exists():
                customer = User.objects.create_user(username=newUserName, email=newUserEmail)
            else:
                customer = User.objects.get(username=newUserName, email=newUserEmail)
            customer.save()

            order = Order.objects.create(customer=customer, complete=False)
            items = []

            SerwMedStore.processCookies(request, items, order, True)

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
            return JsonResponse('Payment incomplete', safe=False)
