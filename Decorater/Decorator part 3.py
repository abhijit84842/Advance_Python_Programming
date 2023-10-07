
# More problem of decorator and its solution..
from functools import wraps
def decorator_functon(any_function):
    @wraps(any_function)
    def wrapper_function(*args , **kwargs):
        ''' this is awesome function..'''
        print("This is wrapper function..")
        return any_function(*args,**kwargs)
    return wrapper_function

@decorator_functon
def add(a,b):
    '''this is add function..'''
    return a+b
print(add(5,6))

print(add.__doc__)
print(add.__name__)
