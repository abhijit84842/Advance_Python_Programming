
# difine a function take any no of list containning numbers...
# [1,2,3] , [4,5,6]
# return avarage..
#(1+4)/2 , (2+5)/2
# Try this program using zip and lambda ...



# Using zip function..
def avarage(l1,l2):
    new_list=[]
    for pair in zip(l1,l2):
        new_list.append(sum(pair)/len(pair))
    return new_list
print(avarage([1,2,3] , [4,5,6]))




# Using *args...
def avarage_num(*args):
    new_list=[]
    for pair in zip(*args):
        new_list.append(sum(pair)/len(pair))
    return new_list
print(avarage_num([1,2,3] , [4,5,6],[7,8,9]))



# Using lambda function ....
avarage_list=lambda *args : [sum(pair)/len(pair) for pair in zip(*args)]
print(avarage_list([1,2,3] , [4,5,6],[9,10,12]))