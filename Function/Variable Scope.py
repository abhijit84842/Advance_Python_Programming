# NOTE:- Can we change global variable value using local variable..???

x=9     # global variable

def func():
    global x
    x=7     # local variable
    return x
print(func())
print(x)