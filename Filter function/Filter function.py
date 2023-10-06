# Filter function..
# NOTE:- We take as a input function name and iterable name in filter function...

def even_num(a):
    return a%2==0

numbers=list(range(1,6))

even_store=tuple(filter(even_num , numbers))
print(even_store)       # Output :- (2, 4)