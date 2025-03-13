
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

# Example - 1
# Check if value exit in dictionaries...
if 'abhijit' in user_info.values():
    print("Present")
else:
    print("Not present")

# Example - 2
# check if value exits in list of values.
if "coco" in user_info["fav_movie"]:
    print("yes")
else:
    print("no")

    