# count
# sort method
# sorted function
# reverse
# clear
# copy




#cout
fruits=["apple","kiwi","banana","orenge","grapes","apple"]
print(fruits.count("apple"))
#Output:- 2


#Sort method
fruits.sort()
print(fruits)
#Output:- ['apple', 'apple', 'banana', 'grapes', 'kiwi', 'orenge']


# sorted function
numbers=list(range(1,11))
numbers.sort()
print(numbers)
#Output:- [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]



# clear method
numbers.clear()
print(numbers)
#Output:- []



# copy method
num1=list(range(20,31))
copy_number=num1.copy()
print(copy_number)
#Output:- [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]