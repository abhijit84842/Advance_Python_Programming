
def square(a):
    return a**2

l=list(range(1,11))

# Solve using map function....
print(list(map(square , l)))


# solve using map and lambda expression...
print(list(map(lambda a : a**2 , l)))


# solve problem using pass a function as a argument..

def my_map(func,l):
    new_list=[]
    for i in l:
        new_list.append(func(i))
    return new_list
print(my_map(square,l))

# Output:- [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]