# decorators-enhance the functionality of other function.. video =169
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
