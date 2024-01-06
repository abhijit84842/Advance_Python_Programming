# Python zip() function returns a zip object. 
# Python's zip() function is a built-in function that is used to combine two or more iterables into a single iterable.

# zip function..

user_info=['user1' , 'user2' ,'user3']
names=['abhijit' , 'sikha' ,'samir']
last_name=['sen' ,'das' ,'das']

print(list(zip(user_info,names,last_name)))                 # convert in list

print(tuple(zip(user_info,names,last_name)))              # convert in tuple


# convert in dictionaries..
information=['user1' , 'user2' ,'user3']
names1=['abhijit' , 'sikha' ,'samir']

print(dict(zip(information,names1)))
