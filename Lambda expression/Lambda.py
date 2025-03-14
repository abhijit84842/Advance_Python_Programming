# Lambda expression(anonymous function)

# NOTE :- Why call anonymous function?
# = because lambda expression has no name so it call anonymous function..

# We use lambda expression with built in function..like map,reduce,filter etc.

# We can use if else with lambda function but we can't use for loop directly with lambda function,intead, we canuse list comprehensions or map(for iteration)

# lambda arguments: expression    

def add(a,b):
    return a+b
print(add(5,2))     # Old method

# Using lambda Expression

add_number=lambda x,y : x+y
print(add_number(5,6))

multiply=lambda a,b : a*b
print(multiply(10,2))