# print the square number 1 to 10 using list
def square(l):
    square=[]
    for i in l:
        square.append(i**2)
    return square
numbers=list(range(1,11))
print(square(numbers))

#Output:- [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]