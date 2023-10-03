def func(a,b):
    return a+b
print(func(8,7) )         # old method

# using args ..
def func2(*args):
    total=0
    for i in args:
        total=total+i
    return total
print(func2(10,20,30))