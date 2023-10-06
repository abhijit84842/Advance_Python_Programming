# filter function with lambda expression...
numbers=list(range(1,21))
odd_store=list(filter(lambda num : num%2 !=0 , numbers))
print(odd_store)