

# Python program to demonstrate
# hybrid inheritance
 
 
class School:
    def func1(self):
        print("Chandrakona Jirat High School.")
 
 
class Student1(School):
    def func2(self):
        print("Studied in class 6 .. ")
 
 
class Student2(School):
    def func3(self):
        print("Studied in class 10.")
 
 
class Student3(Student1, School):
    def func4(self):
        print("Studied in class 6 SEC B..")
 
 
# Driver's code
object = Student3()
object.func1()
object.func2()