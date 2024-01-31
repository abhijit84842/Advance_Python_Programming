# Method Overriding -> Whenever we writing a method in super class and sub class in such a way the method name and the parameter are must be same. thats call method overriding. its is run time polymorphism.



class Animal:
    def speak(self):
        raise NotImplementedError("Subclass must implement this method")
 
class Dog(Animal):
    def speak(self):
        return "Woof!"
 
class Cat(Animal):
    def speak(self):
        return "Meow!"
 

# Create a list of Animal objects
animals = [Dog(), Cat()]
 
# Call the speak method on each object
for i in animals:
    print(i.speak())