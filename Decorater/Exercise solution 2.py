# PROBLEM=Calculate the program execute time using decorator function...

from functools import wraps
import time

def decorator_func(any_function):
    def wrapper_func(*args,**kwargs):
        print(f"exicuting function name : {any_function.__name__}")

        t1=time.time()

        value_return=any_function(*args , **kwargs)

        t2=time.time()
        total=t1-t2
        print(f"This function took total {total} scounds..")
        return value_return
    return wrapper_func


@decorator_func

def square(n):
    return [i**2 for i in range(1,n+1)]

print(square(100))



