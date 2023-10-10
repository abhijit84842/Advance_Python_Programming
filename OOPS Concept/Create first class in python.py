class Person:

    def __init__(self,fisrt_name,last_name, age):
        # instance variable declear.
        self.fname=fisrt_name
        self.lname=last_name
        self.age=age
p1=Person('Abhijit','Das',23)
p2=Person('Ripam', 'Kundu',23)
print(p1.fname)
print(p2.fname)
