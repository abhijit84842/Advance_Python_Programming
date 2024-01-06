# What is exception?
# = Execution time error is called exception.

# try , except 

while True:
    try:
        age=int(input("Enter your age : "))
        break
    except ValueError:
        print("Maybe you entered string instead of number , try again..")
    except:
        print("Unexpected error..")
if age > 18:
    print("You can play this game ...")
else:
    print("You can't play this game")
    