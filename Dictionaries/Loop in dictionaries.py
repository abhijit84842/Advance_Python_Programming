user_info={
    "name" : "abhijit",
    "age" : 24,
    "fav_tone" : ['money hesist' , 'farari'],
    "fav_movie" : ['coco', 'kimi']
}

for i in user_info:
    print(i)        # to print the key only


for i in user_info.values():
    print(i)        # to print the values only


# for loop using items() "to print key and value both at a time"
for i, j in user_info.items():
    print(f"Key is ={i} and Value is ={j}")

