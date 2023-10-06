# Lambda expression(anonymous function)

# NOTE :- Why call anonymous function?
# = because lambda expression has no name so it call anonymous function..

# We use lambda expression with built in function..like map,reduce,filter etc.

def add(a,b):
    return a+b
print(add(5,2))     # Old method

# Using lambda Expression

add_number=lambda x,y : x+y
print(add_number(5,6))

multiply=lambda a,b : a*b
print(multiply(10,2))