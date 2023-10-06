
# Map function..

numbers=[1,2,3,4,5,6]

def square(a):
    return a**2
#print(square(1))
#print(square(2))
#print(square(3))



# Using map function..
# NOTE:- We take as a argument function name and iterable name in map function..

def square_num(num):
    return num**2
square_list=list(map(square_num , numbers))
print(square_list)