# To write raise keyword we occur error in program...
def add(a,b):
    if (type(a)==int and type(b)==int):
        return a+b
    else:
        raise TypeError("oops you are passing wrong data type")

print(add(2,4))

print(add("2","4"))
