class Laptop:
    def __init__(self,brand_name,model_no,price):
        self.brand_name=brand_name
        self.model_no=model_no
        self.price=price

    def apply_discount(self,num):       # create a new method.
        off_price=(num/100)*self.price
        return self.price - off_price
l1=Laptop("Hp","179txn",50000)
l2=Laptop('Lenovo','1520leti',40000)
print(l1.apply_discount(10))
print(l1.apply_discount(20))
