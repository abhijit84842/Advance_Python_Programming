# take the input from user by comma separeted

name, age=input("enter your name and age: ").split(",")

print(f"Your name is {name} and age is {int(age)}")