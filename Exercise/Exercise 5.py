# define a function that take a list of word as argument...
# return list with reverse of every element in that list..

# example
#["abc","xuv","zyx"]

def func(l):
    reverse_element=[]
    for i in l:
        reverse_element.append(i[::-1])
    return reverse_element
words=["abc","xuv","zyx"]
print(func(words))