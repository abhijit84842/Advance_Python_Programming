class Employee:
    def __init__(self):
        self.__name="Abhijit Das"               # To make Private use __
    

e1=Employee()
#print(e1.__name)  # can't not access directly..


print(e1._Employee__name)   # Also it call Name Mangling       # but can be access it indirectly.