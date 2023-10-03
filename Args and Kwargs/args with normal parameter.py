# *args with normal parameter...

def func(num,*args):
    multiply=1
    for i in args:
        multiply *=i
    return multiply

print(func(4,2,3,6))