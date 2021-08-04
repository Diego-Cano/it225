# CUSTOMER CLASS
class Customer():

    def __init__(self, customername, customeraddress):
        self.customername= customername
        self.customeraddress= customeraddress
    
    def getCustomerName(self):
        return self.customername
    
    def getCustomerAddress(self):
        return self.customeraddress
    
    def __str__(self):
        return self.customername + ': ' + self.customeraddress
