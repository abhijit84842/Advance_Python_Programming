# count how many instance is created...

class Car:
    instance_count=0        # class variable
    def __init__(self,name,oil_type,price):
        Car.instance_count +=1
        self.car_name=name
        self.oil=oil_type
        self.price=price

c1=Car('Datsun Redi-go','Pertol',400000)
c2=Car('BMW','Disel',2500000)
print(Car.instance_count)
