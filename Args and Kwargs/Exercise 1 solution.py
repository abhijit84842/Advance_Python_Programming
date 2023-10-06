# define a function..
# input
 
# num , iterable(tuple,list) contaning numbers as args


# example
#nums=[1,2,3]
# to_power(3,*num)

# output
#list...>[1,8,27]


# if user did not pass any args then give a sms user 'hey you didn't pass any args'

# else 
# return list

# NOTE: USE LIST COMPREHENSION..

def func(num,*args):
    if args:
        return [i**num for i in args]
    else:
        return "You did't pass any argument"
numbers=[1,2,3,4,5]
print(func(3,*numbers))