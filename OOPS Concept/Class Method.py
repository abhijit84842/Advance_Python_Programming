class Person:
    count_instance=0        # class variable/class atribute..
    def __init__(self,first_name,last_name,age):

        Person.count_instance +=1

        self.fname=first_name
        self.lname=last_name
        self.age=age

    @classmethod        # call the decorators
    def inst_count(cls):            # class method
        return f"You have created {cls.count_instance} instance of {cls.__name__} class"

    def full_name(self):
        return self.fname + self.lname
    def above_age(self):
        return self.age > 19
    
p1=Person('Ayan', 'Munshi',23)
p2=Person('Abhijit','Das',24)

print(Person.inst_count())        # to call the class method..

print(p1.full_name())         # to call the object/instance method..

print(p2.above_age())
