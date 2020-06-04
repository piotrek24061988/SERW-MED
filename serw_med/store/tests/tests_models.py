import unittest
from .. import models
from django.contrib.auth.models import User
from django.core.exceptions import MultipleObjectsReturned


class StoreModelsTestCases(unittest.TestCase):
    def test_first_product(self):
        # Setup
        productName = 'Voucher konsultacyjny jednorazowy'
        testPrice = 100
        testProduct = None
        # Run
        if not models.Product.objects.filter(name=productName).exists():
            testProduct = models.Product(name=productName, price=testPrice, image='store/voucher.jpg')
            testProduct.save()
        else:
            testProduct = models.Product.objects.get(name=productName)
        # Check
        self.assertEqual(testProduct.name, productName)
        self.assertEqual(testProduct.price, testPrice)

    def test_second_product(self):
        # Setup
        productName = 'Abonament konsultacyjny miesięczny'
        testPrice = 500
        testProduct = None
        # Run
        if not models.Product.objects.filter(name=productName).exists():
            testProduct = models.Product(name=productName, price=testPrice, image='store/abonament.jpg')
            testProduct.save()
        else:
            testProduct = models.Product.objects.get(name=productName)
        # Check
        self.assertEqual(testProduct.name, productName)
        self.assertEqual(testProduct.price, testPrice)

    def test_product_str(self):
        # Setup
        productName = 'ExampleTestProduct1'
        testPrice = 00.01
        testProduct = None
        # Run
        if not models.Product.objects.filter(name=productName).exists():
            testProduct = models.Product(name=productName, price=testPrice, digital=True)
            testProduct.save()
        else:
            testProduct = models.Product.objects.get(name=productName)
        # Check
        self.assertEqual(testProduct.__str__(), productName)

    def test_order(self):
        # Setup
        testUsername = 'StoreTestCustomer1'
        testUser = None
        testOrder = None
        testProduct = None
        # Run
        if not User.objects.filter(username=testUsername).exists():
            testUser = User.objects.create_user(testUsername, testUsername + '@gmail.com', '1234')
        else:
            testUser = User.objects.get(username=testUsername)
        response = User.objects.filter(username=testUsername).first()
        # Check
        self.assertEqual(response, testUser)
        # Run
        if not models.Order.objects.filter(customer=testUser).exists():
            testOrder = models.Order(customer=testUser)
        else:
            testOrder = models.Order.objects.get(customer=testUser)
        # Check
        self.assertEqual(testOrder.customer, testUser)
        self.assertNotEqual(testOrder.__str__(), None)

    def test_order_item(self):
        # Setup
        testUsername = 'StoreTestCustomer2'
        productName = 'ExampleTestProduct2'
        testPrice = 11.22
        testUser = None
        testOrder = None
        testProduct = None
        testOrderItem = None
        # Run
        if not models.Product.objects.filter(name=productName).exists():
            testProduct = models.Product(name=productName, price=testPrice, digital=True)
            testProduct.save()
        else:
            testProduct = models.Product.objects.get(name=productName)
        # Check
        self.assertEqual(testProduct.name, productName)
        self.assertEqual(testProduct.price, testPrice)
        # Run
        if not User.objects.filter(username=testUsername).exists():
            testUser = User.objects.create_user(testUsername, testUsername + '@gmail.com', '1234')
        else:
            testUser = User.objects.get(username=testUsername)
        response = User.objects.filter(username=testUsername).first()
        # Check
        self.assertEqual(response, testUser)
        # Run
        if not models.Order.objects.filter(customer=testUser).exists():
            testOrder = models.Order(customer=testUser)
        else:
            testOrder = models.Order.objects.get(customer=testUser)
        # Check
        self.assertEqual(testOrder.customer, testUser)
        # Run
        if not models.OrderItem.objects.filter(product=testProduct).exists():
            testOrderItem = models.OrderItem(product=testProduct, order=testOrder)
        else:
            try:
                testOrderItem = models.OrderItem.objects.get(product=testProduct)
            except MultipleObjectsReturned:
                testOrderItem = models.OrderItem.objects.filter(product=testProduct).first()
        # Check
        self.assertEqual(testOrderItem.product, testProduct)

    def test_shipping_address(self):
        # Setup
        testUsername = 'StoreTestCustomer3'
        testAddress = 'Grobla 8/10'
        testZipcode = '85-305'
        testNumber = '537240688'
        testCity = 'Bydgoszcz'
        testUser = None
        testOrder = None
        testShipping = None
        simpleCase = False
        # Run
        if not User.objects.filter(username=testUsername).exists():
            testUser = User.objects.create_user(testUsername, testUsername + '@gmail.com', '1234')
        else:
            testUser = User.objects.get(username=testUsername)
        response = User.objects.filter(username=testUsername).first()
        # Check
        self.assertEqual(response, testUser)
        # Run
        if not models.Order.objects.filter(customer=testUser).exists():
            testOrder = models.Order(customer=testUser)
        else:
            try:
                testOrder = models.Order.objects.get(customer=testUser)
            except MultipleObjectsReturned:
                testOrder = models.Order.objects.filter(customer=testUser).first()
        # Check
        self.assertEqual(testOrder.customer, testUser)
        # Run
        if not models.ShippingAddress.objects.filter(customer=testUser).exists():
            testShipping = models.ShippingAddress(customer=testUser, order=testOrder, address=testAddress,
                                                  city=testCity, zipcode=testZipcode, number=testNumber)
        else:
            try:
                testShipping = models.ShippingAddress.objects.get(customer=testUser)
            except MultipleObjectsReturned:
                testShipping = models.ShippingAddress.objects.filter(customer=testUser).first()
                simpleCase = True
        # Check
        self.assertEqual(testShipping.customer, testUser)
        self.assertEqual(testShipping.order, testOrder)
        if not simpleCase:
            self.assertEqual(testShipping.address, testAddress)
            self.assertEqual(testShipping.city, testCity)
            self.assertEqual(testShipping.zipcode, testZipcode)
            self.assertEqual(testShipping.number, testNumber)
            self.assertEqual(testShipping.__str__(), testAddress)
