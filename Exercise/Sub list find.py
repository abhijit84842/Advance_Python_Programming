# define a funtion ..
# [1,2,3,[1,2],[3,4]] input
# output---> how many list in list..
# using type function

def sublist_count(l):
    count=0
    for i in l:
        if type(i)==list:
            count=count+1
    return count
mixed=[1,2,3,[1,2],[3,4]]
print(sublist_count(mixed))