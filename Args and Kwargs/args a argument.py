def multiply_nums(*args):
    multiply=1
    for i in args:
        multiply *=i
    return multiply
num=list(range(1,11))
print(multiply_nums(*num))       # to unpack num we use *
