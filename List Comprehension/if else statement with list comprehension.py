# List comprehension with if else statement..

# Using normal method...
numbers=list(range(1,11))

new_list=[]
for i in numbers:
    if i%2==0:
        new_list.append(i**2)
    else:
        new_list.append(-1)
print(new_list)

# Using this program list comprehension...

new_list1=[i**2 if i%2==0 else -1 for i in numbers]
print(new_list1)

