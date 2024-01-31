# Hierarchical inheritance -> In which 1 single base class and multiple derived class

class Car:
    def __init__(self,name, brand):
        self.name=name
        self.brand=brand

    def Carname(self):
        print(f"The car name is {self.name}")

    def BrandName(self):
        print(f"The Brand name is {self.brand}")

    def Ac(self):
        print("Ac is Available")


class BMW(Car):
    def Music(self):
        print("Music is Available")


class Audi(Car):
    def Airbag(self):
        print("6 Airbags are available")



bmw1=BMW("bMW 40X1" , "BMW")
bmw1.Music()
bmw1.Ac()


ad1=Audi("ADUI 80XIT10" , "AUDI")
ad1.Ac()
ad1.Airbag()



