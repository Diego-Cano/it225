# PAYMENT CLASS

class Payment():

    def __init__(self, paymentmethod, paymentamount, promocode):
        self.paymentmethod= paymentmethod
        self.paymentamount= paymentamount
        self.promocode= promocode
    
    def getPaymentAmount(self):
        return self.paymentamount
    
    def getPaymentMethod(self):
        return self.paymentmethod
    
    def getPaymentPromoCode(self):
        return self.promocode

    def __str__(self):
        self.paymentamount=round(self.paymentamount,2)
        message= "Your total amount will be " + str(self.paymentamount)
        return message
