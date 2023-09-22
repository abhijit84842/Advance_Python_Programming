# filter the odd and even numbers from list..
# define a function
# input
# list---->[1,2,2,4,5,6,7]

# output----->[[1,3,5,7],[2,4,6]]

def odd_even(l):
    odd_num=[]
    even_num=[]
    for i in l:
        if i%2==0:
            even_num.append(i)
        else:
            odd_num.append(i)
    output=[even_num,odd_num]
    return output
numbers=list(range(1,21))
print(odd_even(numbers))

#Output:- [[2, 4, 6, 8, 10, 12, 14, 16, 18, 20], [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]]
