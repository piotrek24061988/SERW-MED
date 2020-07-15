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
        testDescription = 'Jednorazowy voucher na dowolną doradczą konsultację telefoniczną, ' + \
                          'zawierającą się w ramach usług oferowanych przez naszą firmę.'
        testUrl = 'store/voucher.jpg'
        # Run
        if not models.Product.objects.filter(name=productName).exists():
            testProduct = models.Product(name=productName, price=testPrice,
                                         image=testUrl, description=testDescription)
            testProduct.save()
        else:
            testProduct = models.Product.objects.get(name=productName)
        # Check
        self.assertEqual(testProduct.name, productName)
        self.assertEqual(testProduct.price, testPrice)
        self.assertIn(testUrl, testProduct.imageURL)

    def test_second_product(self):
        # Setup
        productName = 'Abonament konsultacyjny miesięczny'
        testPrice = 500
        testProduct = None
        testDescription = 'Miesięczny voucher na dowolne doradcze konsultacje telefoniczne, ' + \
                          'zawierające się w ramach usług oferowanych przez naszą firmę.'
        testUrl = 'store/abonament.jpg'
        # Run
        if not models.Product.objects.filter(name=productName).exists():
            testProduct = models.Product(name=productName, price=testPrice,
                                         image=testUrl, description=testDescription)
            testProduct.save()
        else:
            testProduct = models.Product.objects.get(name=productName)
        # Check
        self.assertEqual(testProduct.name, productName)
        self.assertEqual(testProduct.price, testPrice)
        self.assertIn(testUrl, testProduct.imageURL)

    def test_product_str(self):
        # Setup
        productName = 'Example Test Product 1'
        testPrice = 00.01
        testProduct = None
        testDescription = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. '+\
                          'Proin nibh augue, suscipit a, scelerisque sed, lacinia in, mi. '+\
                          'Cras vel lorem. Etiam pellentesque aliquet tellus. Phasellus pharetra nulla ac diam. ' +\
                          'Quisque semper justo at risus. Donec venenatis, turpis vel hendrerit interdum, '+\
                          'dui ligula ultricies purus, sed posuere libero dui id orci. ' +\
                          'Nam congue, pede vitae dapibus aliquet, elit magna vulputate arcu, '+\
                          'vel tempus metus leo non est. Etiam sit amet lectus quis est congue mollis. '+\
                          'Phasellus congue lacus eget neque. Phasellus ornare, ante vitae consectetuer consequat, '+\
                          'purus sapien ultricies dolor, et mollis pede metus eget nisi. Praesent sodales velit quis augue. '+\
                          'Cras suscipit, urna at aliquam rhoncus, urna quam viverra nisi, in interdum massa nibh nec erat.'
        # Run
        if not models.Product.objects.filter(name=productName).exists():
            testProduct = models.Product(name=productName, price=testPrice, digital=True, description=testDescription)
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
        self.assertEqual(testOrder.get_cart_total, 0)
        self.assertEqual(testOrder.get_cart_items, 0)
        self.assertEqual(testOrder.shipping, False)

    def test_order_item(self):
        # Setup
        testUsername = 'StoreTestCustomer2'
        productName = 'Example Test Product 2'
        testDescription = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. '+\
                          'Proin nibh augue, suscipit a, scelerisque sed, lacinia in, mi. '+\
                          'Cras vel lorem. Etiam pellentesque aliquet tellus. Phasellus pharetra nulla ac diam. ' +\
                          'Quisque semper justo at risus. Donec venenatis, turpis vel hendrerit interdum, '+\
                          'dui ligula ultricies purus, sed posuere libero dui id orci. ' +\
                          'Nam congue, pede vitae dapibus aliquet, elit magna vulputate arcu, '+\
                          'vel tempus metus leo non est. Etiam sit amet lectus quis est congue mollis. '+\
                          'Phasellus congue lacus eget neque. Phasellus ornare, ante vitae consectetuer consequat, '+\
                          'purus sapien ultricies dolor, et mollis pede metus eget nisi. Praesent sodales velit quis augue. '+\
                          'Cras suscipit, urna at aliquam rhoncus, urna quam viverra nisi, in interdum massa nibh nec erat.'
        testPrice = 11.22
        testQuantity = 1
        testUser = None
        testOrder = None
        testProduct = None
        testOrderItem = None
        # Run
        if not models.Product.objects.filter(name=productName).exists():
            testProduct = models.Product(name=productName, price=testPrice, digital=True, description=testDescription)
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
            testOrderItem = models.OrderItem(product=testProduct, order=testOrder, quantity=testQuantity)
        else:
            try:
                testOrderItem = models.OrderItem.objects.get(product=testProduct)
            except MultipleObjectsReturned:
                testOrderItem = models.OrderItem.objects.filter(product=testProduct).first()
        # Check
        self.assertEqual(testOrderItem.product, testProduct)
        self.assertEqual(testOrderItem.get_total, testPrice)

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
