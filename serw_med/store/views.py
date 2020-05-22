from django.shortcuts import render


class SerwMedStore:
    def __init__(self):
        pass

    @staticmethod
    def store(request):
        context = {}
        return render(request, 'store.html', context)

    @staticmethod
    def cart(request):
        context = {}
        return render(request, 'cart.html', context)

    @staticmethod
    def checkout(request):
        context = {}
        return render(request, 'checkout.html', context)

