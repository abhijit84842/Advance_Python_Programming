# Normal method...
numbers=list(range(1,11))
even_num=[]
for i in numbers:
    if i%2==0:
        even_num.append(i)
print(even_num)


# Using list comprhension
even_num=[i for i in numbers if i%2==0]
odd_num=[i for i in numbers if i%2 !=0]
print(even_num)
print(odd_num)