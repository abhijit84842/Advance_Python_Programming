# Where we use self and where we use class variable..?
# => for any particular momvent we use self ..therwise we use class variable..

class Laptop:
    discount_percent=10
    def __init__(self,brand,model,ram,price):
        self.brand=brand
        self.model=model
        self.ram=ram
        self.price=price
    
    def apply_discount(self):
        # Use self.discount_percent to discount a particular product..
        off_price=(self.discount_percent/100)*self.price
        return self.price-off_price
    

#Laptop.discount_percent=0       #'''To off the discount..'''

l1=Laptop("Hp" ,"abut15tx" ,"8 Gb" , 100)

l1.discount_percent=5       # 5%  discount on only hp laptop

l2=Laptop("Dell", "dft5txt" ,"12 Gb", 200)

print(l1.apply_discount())
print(l2.apply_discount())