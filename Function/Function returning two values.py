# Function returning two values..
def func1(int1,int2):
    add=int1 + int2
    multiply=int2 * int1
    return add , multiply

add,multiply=func1(2,6)
print(f"add value is : {add} & multiply value is : {multiply}")