# check all numbers in list is even or odd

numbers1=[2,4,1,8,10]

even=all([i%2==0 for i in numbers1])        # when we check all numbers are even.. using all function
print(even)     # Output:- Flase



numbers2=[1,3,4,5,7]
even1=any([i%2==0 for i in numbers2])       # when we check any one numbers is even in list..
print(even1)        # Output:- True
