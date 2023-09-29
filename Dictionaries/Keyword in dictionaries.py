
user_info={
    "name" : "abhijit",
    "age" : 24,
    "fav_tone" : ['money hesist' , 'farari'],
    "fav_movie" : ['coco', 'kimi']
}


# Check if key exit in dictionaries...
if "name" in user_info:
    print("Yes")
else:
    print("No")

# Check if value exit in dictionaries...
if 'abhijit' in user_info.values():
    print("Present")
else:
    print("Not present")

    