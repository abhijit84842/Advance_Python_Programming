# We use enumerate function with for loop to track position of our item initerable..
# Python enumerate() function returns an enumerated object.


# how we can do this without enumerate function...
names=['abhijit' ,'subhajit' ,'sikha' ,'samir', 'raja']

'''
# Old method..
pos=0
for i in names:
    print(f"{pos}......>{i}")
    pos=pos+1

    
'''

# Using enumerate function..
for pos , i in enumerate(names):
    print(f"{pos}....>{i}")



# ex=> 2
    # create a list of fruits  
fruits = ['apple', 'banana', 'cherry']  
  
# iterate over the list using the enumerate() function  
# the enumerate() function returns a tuple containing the index and value of each element  
for pos, i in enumerate(fruits):  
    # print the index and value of each element  
    print(pos, i)
    


# ex=> 3
numbers = [1, 2, -3, 4, -5, 6]  
for pos, i in enumerate(numbers):
    print(pos, i)