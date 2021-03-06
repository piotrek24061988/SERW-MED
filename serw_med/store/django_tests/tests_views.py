from django.test import TestCase, Client
from django.urls import reverse


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