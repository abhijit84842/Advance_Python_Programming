winning_number=27
user_input=int(input("Enter the number : "))
if user_input==winning_number:
    print('You win !..')
else:
    if user_input < winning_number:
        print("too low")
    else:
        print("too high!..")