# ITEM CLASS
class Item():

    def __init__(self, itemnum, itemname, intemprice, itemdetail):
        self.itemnum=itemnum
        self.itemname=itemname
        self.itemprice=itemprice
        self.itemdetail=itemdetail
    
    def getItemNumber(self):
        return self.itemnum
    
    def getItemName(self):
        return self.itemname
    
    def getItemPrice(self):
        return self.itemprice
    
    def getItemDetail(self):
        return self.detail
    
    def __str__(self):
        return self.itemname + ': ' + self.detail
    