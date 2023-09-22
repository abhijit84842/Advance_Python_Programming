# common element finder function....
# define a function which take 2 list as input and return a list 
# which contain common element of both list..
# example 
# input....> [1,2,5,8] ,[1,2,7,6]
# output ....> [1,2]

def common_ele(l1,l2):
    output=[]
    for i in l1:
        if i in l2:
            output.append(i)
    return output

print(common_ele([1,2,5,8] , [1,2,7,6])) 