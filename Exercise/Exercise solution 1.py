# Take the integer input from the user & find out the avarage

num1=int(input("Enter the first number : "))
num2=int(input("Enter the secound number : "))
num3=int(input("Enter the third number : "))

int(num1) + int(num2) + int(num3)

print(f"The avarage is {(int(num1) + int(num2) + int(num3)) /3}")


#NOTE :- take input in one line..
num1 ,num2 , num3=input("Enter three number by coma separated :").split(",")
print(f"Avarage number is : {(int(num1) + int(num3) + int(num3)) /3}")

