class Car:
    def __init__(self,name, brand):
        self.name=name
        self.brand=brand

    def Carname(self):
        print(f"The car name is {self.name}")

    def BrandName(self):
        print(f"The Brand name is {self.brand}")

class New_Features1(Car):

    def Ac(self):
        print("Ac is Available")
    def Music(self):
        print("Music is Available")

class New_Features2(New_Features1):
    def Airbag(self):
        print("6 Airbags are available")


n2=New_Features2("Alto", "SUZUKI")
n2.Carname()
n2.BrandName()
n2.Music()
n2.Airbag()