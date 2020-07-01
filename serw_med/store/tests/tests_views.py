from django.test.client import RequestFactory
from django.contrib.auth.models import AnonymousUser
import unittest
import io
from .. import views


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
