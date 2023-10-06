
# Find the grater number list..

l1=[1,3,5,7]
l2=[2,4,6,8]

new_list=[]
for pair in zip(l1,l2):
    new_list.append(max(pair))
print(new_list)         # Output :- [2, 4, 6, 8]