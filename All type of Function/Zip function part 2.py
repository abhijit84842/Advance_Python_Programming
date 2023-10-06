
l= [(1,2) , (3,4) , (5,6), (7,8)]

# NOTE:- Use * operator with zip..(use for unpack zip)

l1,l2=list(zip(*l))
print(list(l1))
print(list(l2))

'''
# Output :- [1, 3, 5, 7]
            [2, 4, 6, 8]
'''
