# decorators-enhance the functionality of other function.. video =169
# In Decorators, functions are passed as an argument into another function and then called inside the wrapper function
# It is also called meta programming where a part of the program attempts to change another part of program at compile time.
#  @ use for decorator


def decorater_function(any_function):
    def wrapper_function():
        print("this is wrapper function..")
        any_function()

    return wrapper_function

@decorater_function     #Shortcut for decorator...
def func1():
    print("this is function 1..")


func1()
