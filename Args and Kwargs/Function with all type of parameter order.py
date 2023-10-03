# function with all parameters..
# very important to understand..

# PADK Rulse
# Parameters.
# *args.
# default parameters.
# **kwargs.

def func(name , *args, last_name='unknown' , **kwargs):
    print(name)
    print(args)
    print(last_name)
    print(kwargs)
print(func('Abhijit' , 11,2,5 , 'das' , age=24 , year=1999))