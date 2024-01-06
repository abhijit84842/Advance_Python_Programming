# raise errors example..
# NotImplementedError..
# abstract method is NotImplementedError in python

class Animal:
    def __init__(self, name):
        self.name=name
    
    def sound(self):
        raise NotImplementedError("You have to define method in subclasses of sound..")

class Dog(Animal):
    def __init__(self,name,breed):
        super().__init__(name)      # use parent class object..
        self.breed=breed

        def sound(self):
            return ('bhow', 'bhow')

class Cat(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed=breed

dog1=Dog("Raja","Spitz")
print(dog1.sound())
