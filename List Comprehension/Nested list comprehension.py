# List comprehension in nested list...
# Create Nested list using list comprehension ...
#  print the inner list 5 times..
# Example : -  numbers=[[1,2,3] , [1,2,3] , [1,2,3] , [1,2,3] , [1,2,3]]



nested_comp=[[i for i in range(1,4)] for j in range(5)]
print(nested_comp)