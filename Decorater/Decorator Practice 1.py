def print_function_data(func):
    def warapper_function(*args, **kwargs):
        print(f"you are calling {func.__name__}")
        print(f"{func.__doc__}")
        return func(*args , **kwargs)
    return warapper_function

@print_function_data
def add(a,b):
    '''this is add function take two parameter and return their sum..'''
    return a+b
print(add(2,10))