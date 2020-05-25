import unittest
from .. import models
from django.contrib.auth.models import User


class StoreModelsTestCases(unittest.TestCase):
    def test_first_customer(self):
        # Setup
        testUsername = 'UsersTestCustomer1'
        testUser = None
        testCustomer = None
        # Run
        if not User.objects.filter(username=testUsername).exists():
            testUser = User.objects.create_user(testUsername, testUsername + '@gmail.com', '1234')
        else:
            testUser = User.objects.get(username=testUsername)
        response = User.objects.filter(username=testUsername).first()
        # Check
        self.assertEqual(response, testUser)
        # Run
        if not models.Customer.objects.filter(user=testUser).exists():
            testCustomer = models.Customer(user=testUser, name=testUsername, email=testUsername + '@gmail.com')
            testCustomer.save()
            # Check
            self.assertEqual(testUsername, testUser.customer.name)
        else:
            testCustomer = models.Customer.objects.get(user=testUser)
        # Check
        self.assertEqual(testCustomer, testUser.customer)

    def test_customer_str(self):
        # Setup
        testUsername = 'UsersTestCustomer2'
        testUser = None
        testCustomer = None
        # Run
        if not User.objects.filter(username=testUsername).exists():
            testUser = User.objects.create_user(testUsername, testUsername + '@gmail.com', '1234')
        else:
            testUser = User.objects.get(username=testUsername)
        response = User.objects.filter(username=testUsername).first()
        # Check
        self.assertEqual(response, testUser)
        # Run
        if not models.Customer.objects.filter(user=testUser).exists():
            testCustomer = models.Customer(user=testUser, name=testUsername, email=testUsername + '@gmail.com')
            testCustomer.save()
        else:
            testCustomer = models.Customer.objects.get(user=testUser)
        # Check
        self.assertEqual(testCustomer.__str__(), testUsername)

    def test_first_product(self):
        # Setup
        productName = 'ExampleTestProduct1'
        testPrice = 11.22
        testProduct = None
        # Run
        if not models.Product.objects.filter(name=productName).exists():
            testProduct = models.Product(name=productName, price=testPrice)
            testProduct.save()
        else:
            testProduct = models.Product.objects.get(name=productName)
        # Check
        self.assertEqual(testProduct.name, productName)
        self.assertEqual(testProduct.price, testPrice)

    def test_product_str(self):
        # Setup
        productName = 'ExampleTestProduct2'
        testPrice = 11.22
        testProduct = None
        # Run
        if not models.Product.objects.filter(name=productName).exists():
            testProduct = models.Product(name=productName, price=testPrice)
            testProduct.save()
        else:
            testProduct = models.Product.objects.get(name=productName)
        # Check
        self.assertEqual(testProduct.__str__(), productName)

    def test_order(self):
        # Setup
        testUsername = 'UsersTestCustomer3'
        testUser = None
        testCustomer = None
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
        if not models.Customer.objects.filter(user=testUser).exists():
            testCustomer = models.Customer(user=testUser, name=testUsername, email=testUsername + '@gmail.com')
            testCustomer.save()
            # Check
            self.assertEqual(testUsername, testUser.customer.name)
        else:
            testCustomer = models.Customer.objects.get(user=testUser)
        # Check
        self.assertEqual(testCustomer, testUser.customer)
        # Run
        if not models.Order.objects.filter(customer=testCustomer).exists():
            testOrder = models.Order(customer=testCustomer)
        else:
            testOrder = models.Order.objects.get(customer=testCustomer)
        # Check
        self.assertEqual(testOrder.customer, testCustomer)
        self.assertEqual(testOrder.customer.user, testUser)
        self.assertNotEqual(testOrder.__str__(), None)

    def test_order_item(self):
        # Setup
        testUsername = 'UsersTestCustomer4'
        productName = 'ExampleTestProductOrder1'
        testPrice = 11.22
        testUser = None
        testCustomer = None
        testOrder = None
        testProduct = None
        testOrderItem = None
        # Run
        if not models.Product.objects.filter(name=productName).exists():
            testProduct = models.Product(name=productName, price=testPrice)
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
        if not models.Customer.objects.filter(user=testUser).exists():
            testCustomer = models.Customer(user=testUser, name=testUsername, email=testUsername + '@gmail.com')
            testCustomer.save()
            # Check
            self.assertEqual(testUsername, testUser.customer.name)
        else:
            testCustomer = models.Customer.objects.get(user=testUser)
        # Check
        self.assertEqual(testCustomer, testUser.customer)
        # Run
        if not models.Order.objects.filter(customer=testCustomer).exists():
            testOrder = models.Order(customer=testCustomer)
        else:
            testOrder = models.Order.objects.get(customer=testCustomer)
        # Check
        self.assertEqual(testOrder.customer, testCustomer)
        self.assertEqual(testOrder.customer.user, testUser)
        # Run
        if not models.OrderItem.objects.filter(product=testProduct).exists():
            testOrderItem = models.OrderItem(product=testProduct, order=testOrder)
        else:
            testOrderItem = models.OrderItem.objects.get(order=testOrder)
        # Check
        self.assertEqual(testOrderItem.order, testOrder)
        self.assertEqual(testOrderItem.product, testProduct)

    def test_shipping_address(self):
        # Setup
        testUsername = 'UsersTestCustomer5'
        testAddress = 'Kowalska 3'
        testZipcode = '12-345'
        testNumber = '123456789'
        testCity = 'Center'
        testUser = None
        testCustomer = None
        testOrder = None
        testShipping = None
        # Run
        if not User.objects.filter(username=testUsername).exists():
            testUser = User.objects.create_user(testUsername, testUsername + '@gmail.com', '1234')
        else:
            testUser = User.objects.get(username=testUsername)
        response = User.objects.filter(username=testUsername).first()
        # Check
        self.assertEqual(response, testUser)
        # Run
        if not models.Customer.objects.filter(user=testUser).exists():
            testCustomer = models.Customer(user=testUser, name=testUsername, email=testUsername + '@gmail.com')
            testCustomer.save()
            # Check
            self.assertEqual(testUsername, testUser.customer.name)
        else:
            testCustomer = models.Customer.objects.get(user=testUser)
        # Check
        self.assertEqual(testCustomer, testUser.customer)
        # Run
        if not models.Order.objects.filter(customer=testCustomer).exists():
            testOrder = models.Order(customer=testCustomer)
        else:
            testOrder = models.Order.objects.get(customer=testCustomer)
        # Check
        self.assertEqual(testOrder.customer, testCustomer)
        self.assertEqual(testOrder.customer.user, testUser)
        # Run
        if not models.ShippingAddress.objects.filter(customer=testCustomer).exists():
            testShipping = models.ShippingAddress(customer=testCustomer, order=testOrder, address=testAddress,
                                                  city=testCity, zipcode=testZipcode, number=testNumber)
        else:
            testShipping = models.ShippingAddress.objects.get(customer=testCustomer)
        # Check
        self.assertEqual(testShipping.customer, testCustomer)
        self.assertEqual(testShipping.order, testOrder)
        self.assertEqual(testShipping.address, testAddress)
        self.assertEqual(testShipping.city, testCity)
        self.assertEqual(testShipping.zipcode, testZipcode)
        self.assertEqual(testShipping.number, testNumber)
        self.assertEqual(testShipping.__str__(), testAddress)