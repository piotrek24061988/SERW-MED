import unittest
from django.urls import reverse, resolve
from .. import views


class StoreUrlsTestCases(unittest.TestCase):

    def test_url_store(self):
        # Setup
        url = reverse('serw-med-store')
        testFunc = views.SerwMedStore.store
        # Run
        resolvedUrl = resolve(url)
        # Check
        self.assertEqual(resolvedUrl.func, testFunc)

    def test_url_cart(self):
        # Setup
        url = reverse('serw-med-cart')
        testFunc = views.SerwMedStore.cart
        # Run
        resolvedUrl = resolve(url)
        # Check
        self.assertEqual(resolvedUrl.func, testFunc)

    def test_url_checkout(self):
        # Setup
        url = reverse('serw-med-checkout')
        testFunc = views.SerwMedStore.checkout
        # Run
        resolvedUrl = resolve(url)
        # Check
        self.assertEqual(resolvedUrl.func, testFunc)

    def test_url_product(self):
        # Setup
        url = reverse('serw-med-product', args=['0'])
        testClass = views.SerwMedStoreProduct
        # Run
        resolvedUrl = resolve(url)
        # Check
        self.assertEqual(resolvedUrl.func.view_class, testClass)

    def test_url_update_item(self):
        # Setup
        url = reverse('serw-med-update-item')
        testFunc = views.SerwMedStore.updateItem
        # Run
        resolvedUrl = resolve(url)
        # Check
        self.assertEqual(resolvedUrl.func, testFunc)

    def test_url_process_order(self):
        # Setup
        url = reverse('serw-med-process-order')
        testFunc = views.SerwMedStore.processOrder
        # Run
        resolvedUrl = resolve(url)
        # Check
        self.assertEqual(resolvedUrl.func, testFunc)
