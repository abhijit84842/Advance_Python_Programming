class Car:
    def __init__(self,name,brand):
        self.name=name
        self.brand=brand

    def car_name(self):
        print(f"The car name is {self.name}")

    def Car_brand(self):
        print(f"The car Brand is {self.brand}")


class EvCar(Car):
    def Electric_vechil(self):
        print("Ev type is - > Fast Charging... ")


e1=EvCar("Alto 800" ,"Nexa")
e1.car_name()
e1.Electric_vechil()