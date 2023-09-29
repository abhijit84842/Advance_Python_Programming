# take a empty dictionary
# then take the input from user
# and print the key and value

user_info={}

name=input("Enter your name : ")
age=int(input("Enter ege : "))
fav_tone=input("Enter your favourite tone : ")
fav_movie=input("Enter fav_movie: ")

user_info['name']=name
user_info['age']=age
user_info['fav_tone']=fav_tone
user_info['fav_movie']=fav_movie

for i , j in user_info.items():
    print(f"{i} : {j}")