# list comprehension....

list1=[]
for i in range(1,11):
    list1.append(i**2)          # when we create list normaly..
print(list1)


# by using list comprehension..
num=[i**2 for i in range(1,11)]
print(num)


#More example..
name=['abhijit' , 'sudip' , 'akash']
new_name=[]
for i in name:
    new_name.append(i[0])
print(new_name)

# Using list comprehension..
new_name1=[i[0] for i in name]
print(new_name1)


