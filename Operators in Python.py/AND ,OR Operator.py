# AND Operator..

user_name=input("Enter your name : ")
password=(input("Enter Your age : "))

if user_name == "admin" and password == "admin":
    print("login successfully")
else:
    print("Not matching")

# OR Operator..
name=input("enter your name : ")
age=int(input("enter your age : "))

if name=="aditya" or age==18:
    print("you are eligible..")
else:
    print("not eligible..")