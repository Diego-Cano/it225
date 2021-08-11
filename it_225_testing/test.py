import unittest
from customer import Customer
from payment import Payment

# CUSTOMER 1
class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.c=Customer('Lily Whites', '928 Wild Rose Dr. Palm Coast, FL 32137')
    
    def test_getCustomerAddress(self):
        self.assertEqual(self.c.getCustomerAddress(), '928 Wild Rose Dr. Palm Coast, FL 32137')
    
    def test_getCustomerName(self):
        self.assertEqual(self.c.getCustomerName(), 'Lily Whites')

# CUSTOMER 2
class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.c=Customer('Josh Goodman', '7625 Greystone Street Mount Vernon, NY 10550')
    
    def test_getCustomerAddress(self):
        self.assertEqual(self.c.getCustomerAddress(), '7625 Greystone Street Mount Vernon, NY 10550')
    
    def test_getCustomerName(self):
        self.assertEqual(self.c.getCustomerName(), 'Josh Goodman')

# PAYMENT 1
class TestPayment(unittest.TestCase):
    def setUp(self):
        self.p=Payment('Cash', 120, 'ab234')
    
    def test_getPaymentAmount(self):
        self.assertEqual(self.p.getPaymentAmount(), 120)
    
    def test_getPaymentMethod(self):
        self.assertEqual(self.p.getPaymentMethod(), 'Cash')
    
    def test_getPaymentPromoCode(self):
        self.assertEqual(self.p.getPaymentPromoCode(), 'ab234')

# PAYMENT 2
class TestPayment(unittest.TestCase):
    def setUp(self):
        self.p=Payment('MasterCard', 54, '4stb5')
    
    def test_getPaymentAmount(self):
        self.assertEqual(self.p.getPaymentAmount(), 54)
    
    def test_getPaymentMethod(self):
        self.assertEqual(self.p.getPaymentMethod(), 'MasterCard')
    
    def test_getPaymentPromoCode(self):
        self.assertEqual(self.p.getPaymentPromoCode(), '4stb5')