while True:
    try:
        age=int(input("Enter your age : "))
    except ValueError:
        print("please type intiger..")
    else:
        print(f"input age is {age}")
        break
    finally:
        print("This is finally block..")
if age > 18:
     print("You cant play this game..")
else:
    print("You can't play this game ...")
    


