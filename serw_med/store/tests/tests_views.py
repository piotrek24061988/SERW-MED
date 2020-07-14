from django.test.client import RequestFactory
from django.contrib.auth.models import AnonymousUser
import unittest
from .. import views
from django.test import TestCase, Client
from django.urls import reverse


class StoreViewsTestCases(unittest.TestCase):
    # Common setup
    request = RequestFactory()
    request.user = AnonymousUser()
    request.method = 'POST'
    setattr(request, 'COOKIES', {})
    request.COOKIES['cart'] = '{"get_cart_total": 0, "get_cart_items": 0, "shipping": "False"}'
    response_status = 200

    def test_store(self):
        # Setup
        response_content = b'Voucher'
        # Run
        response = views.SerwMedStore.store(StoreViewsTestCases.request)
        # Check
        self.assertEqual(response.status_code, StoreViewsTestCases.response_status)
        self.assertIn(response_content, response.content)

    def test_cart(self):
        # Setup
        response_content = b'Produkty'
        # Run
        response = views.SerwMedStore.cart(StoreViewsTestCases.request)
        # Check
        self.assertEqual(response.status_code, StoreViewsTestCases.response_status)
        self.assertIn(response_content, response.content)

    def test_checkout(self):
        # Setup
        response_content = b'Podsumowanie'
        # Run
        response = views.SerwMedStore.checkout(StoreViewsTestCases.request)
        # Check
        self.assertEqual(response.status_code, StoreViewsTestCases.response_status)
        self.assertIn(response_content, response.content)


class StoreViewsDjangoTestCases(TestCase):
    # Common setup
    def setUp(self):
        self.client = Client()

    def test_store_GET(self):
        # Setup
        url = reverse('serw-med-store')
        # Run
        response = self.client.get(url)
        # Check
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'store.html')

    def test_cart_GET(self):
        # Setup
        url = reverse('serw-med-cart')
        # Run
        response = self.client.get(url)
        # Check
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cart.html')

    def test_checkout_GET(self):
        # Setup
        url = reverse('serw-med-checkout')
        # Run
        response = self.client.get(url)
        # Check
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout.html')

    def test_fake_product_GET(self):
        # Setup
        url = reverse('serw-med-product', args=['0'])
        # Run
        response = self.client.get(url)
        # Check
        self.assertEqual(response.status_code, 404)
        self.assertTemplateNotUsed(response, 'product_single.html')

    def test_update_item_GET(self):
        # Setup
        url = reverse('serw-med-update-item')
        # Run
        response = self.client.get(url)
        # Check
        self.assertEqual(response.status_code, 200)