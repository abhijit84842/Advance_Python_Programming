name ,age =input('enter user name and age : ').split(",")
age1=int(age)
if age1 > 10 and (name[0]=='a' or name[0]=='A'):
    print("You can watch the movie..")
else:
    print("You can't watch the movie..")