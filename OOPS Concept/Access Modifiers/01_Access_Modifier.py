
# Private Modifire -> Use Double Underscore(__)
class Employee:
    def __init__(self):
        self.__name="Abhijit Das"               # To make Private use __
    

e1=Employee()
#print(e1.__name)  # can't not access directly..


print(e1._Employee__name)   # Also it call Name Mangling       # but can be access it indirectly.



# Protected -> use Single UnderScore(_)
class Student:
    def __init__(self):
        self.name1="Aditya Sen"

    def _NickName(self):
        return "Rintu"
    

class Subject(Student):
    pass


obj1=Student()
obj2=Subject()

print(obj1.name1)
print(obj2._NickName())