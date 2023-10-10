# 'Class method as a constructor...
# create your own constructor instead of init constructor...


class Person:
    count_instance=0        #class variable
    def __init__(self,first_name,last_name,age):
        Person.count_instance +=1
        self.fname=first_name
        self.lname=last_name
        self.age=age

    @classmethod            # create my own constructor..
    def new_constructor(cls,str):
       first,last,age=str.split(',')
       print("f{first} , {last} , {age}")
       return cls(first,last,age)
    
    @classmethod
    def instance_count(cls):     # as a object we pass class name or cls(acording to the conviniant we right "cls")
        return f"You have created {cls.count_instance} instance of {cls.__name__} class"
    
    def full_name(self):
        return  f"full name is {self.fname} {self.lname}"
    

p1=Person("Abhijit","Das",23)

print(Person.instance_count())      # calling the class method

print(p1.full_name())           # calling the object/instance method


new_p3=Person.new_constructor("Suman , Bisal , 35")
print(new_p3.full_name())

    
