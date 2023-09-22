# using reverse method()

def reverse_list(l):
    l.reverse()
    return l
numbers=list(range(1,11))
print(reverse_list(numbers))


#Using append and pop method
def func(l1):
    reversed_items=[]
    for i in range(len(l1)):
        pop_items=l1.pop()
        reversed_items.append(pop_items)
    return reversed_items

num1=list(range(20,41))
print(func(num1))