age=int(input("Enter your age : "))

if age==0:
    print("You can't get tickit..")
elif 1<age<3:
    print('your tickit is free..')
elif 4<age<=10:
    print("Your tickit price is 150..")
elif 11<age<=60:
    print("Your tickit price is 250..")
elif 60<age:
    print("your tickit price is 200..")