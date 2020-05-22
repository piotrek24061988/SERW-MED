import unittest
from .. import views
from common import stubs


class StoreViewsTestCases(unittest.TestCase):
    # Common setup
    request = stubs.RequestStub
    response_status = 200

    def test_store(self):
        # Setup
        StoreViewsTestCases.request.method = 'POST'
        response_content = b'sklep'
        # Run
        response = views.SerwMedStore.store(StoreViewsTestCases.request)
        # Check
        self.assertEqual(response.status_code, StoreViewsTestCases.response_status)
        self.assertIn(response_content, response.content)

    def test_cart(self):
        # Setup
        StoreViewsTestCases.request.method = 'POST'
        response_content = b'cart'
        # Run
        response = views.SerwMedStore.cart(StoreViewsTestCases.request)
        # Check
        self.assertEqual(response.status_code, StoreViewsTestCases.response_status)
        self.assertIn(response_content, response.content)

    def test_checkout(self):
        # Setup
        StoreViewsTestCases.request.method = 'POST'
        response_content = b'checkout'
        # Run
        response = views.SerwMedStore.checkout(StoreViewsTestCases.request)
        # Check
        self.assertEqual(response.status_code, StoreViewsTestCases.response_status)
        self.assertIn(response_content, response.content)
