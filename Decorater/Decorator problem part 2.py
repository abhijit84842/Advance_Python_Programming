
# some problem of decorator...and solution..

def decorator_function(any_funtion):
    def wrapper_function(*args ,**kwargs):
        print("This is wrapper function ..")
        return any_funtion(*args , **kwargs)    
    return wrapper_function

@decorator_function
def func1(a):
    print(f"This is function 1 with argument {a}")

func1(7)


@decorator_function
def add_func(*args):
    return sum(args)
print(add_func(8,4,5,6,10,11,10,12))