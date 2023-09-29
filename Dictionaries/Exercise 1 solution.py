# difine a function that take two number(n)
# return a dictionaries containg cube of numbers from 1 to n

# example
# cube_finder(3)
#{1:1,2:8,3:27}

def cube_finder(n):
    cube={}
    for i in range(1,1+n):
        cube[i]=i**3
    return cube
print(cube_finder(10))