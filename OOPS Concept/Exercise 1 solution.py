# create a clas with atributes like brand name,model name,price
# create two object/instance of your laptop class.

class Laptop:
    def __init__(self,brand_name,model_no,price):
        #instance variable declear...
        self.brand_name=brand_name
        self.model_no=model_no
        self.price=price

l1=Laptop("HP","179TTX",45000)
l2=Laptop("Dell","D451ftx",50000)

print(l1.brand_name,l1.model_no,l1.price)

print(l2.brand_name,l2.brand_name,l2.price)