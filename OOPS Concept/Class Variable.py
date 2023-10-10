# class variable Part 1

class Circle:
    def __init__(self,radius,pi):
        self.radius=radius
        self.pi=pi
    def cal_circumfrance(self):
        return 2*self.pi*self.radius        # Rule of = 2*pi*r
c1=Circle(4,3.4)    # Pi value is always same..
c2=Circle(5,3.4)
print(c1.cal_circumfrance())        # Output:-27.2
print(c2.cal_circumfrance())        # Output:-34.0


# NOTE:- After declear class variable..

class Circle1:
    pi=3.4  # class variable
    def __init__(self,radius):
        self.radius=radius
    def calculate_circumfrance(self):
        return 2*Circle1.pi*self.radius

c03=Circle1(6)
c04=Circle1(7)
print(c03.calculate_circumfrance())     # Output:- 40.8
print(c04.calculate_circumfrance())     # Output:- 47.6
