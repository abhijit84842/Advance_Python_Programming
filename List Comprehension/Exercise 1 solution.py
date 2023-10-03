
# Take a list using list comprehension and reverse  the list..


# Normal method..
def reverse_list(l):
    new_list=[]
    for i in l:
        new_list.append(i[::-1])
    return new_list

name=['abhijit','pradipta']

print(reverse_list(name))



# Using list comprehension..
word=['abc' , 'edg']
reversed_items=[i[::-1] for i in word]
print(reversed_items)