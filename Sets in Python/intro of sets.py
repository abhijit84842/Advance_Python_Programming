# A Set in Python programming is an unordered collection data type that is iterable, mutable and has no duplicate elements. 
# The major advantage of using a set, as opposed to a list,
# This is based on a data structure known as a hash table. Since sets are unordered, we cannot access items using indexes as we do in lists.
# Time Complexity: O(1)
# We can also use the pop() method to remove the item. Generally, the pop() method will always remove the last item but the set is unordered, we can't determine which element will be popped from set.

# set is Mutable So, we can change orginal set.

# ex=>=1 
var = {"Eat", "Coding", "Sleep"}
print(type(var))

# The Python set() method is used for type casting.
myset=set(["a","b","c"])
print(myset)        # Output=> {'b', 'c', 'a'}



# Empty curly braces will create dictionary  
set3 = {}  
print(type(set3))  # <class 'dict'>
  
# Empty set using set() function  
set4 = set()  
print(type(set4))   #<class 'set'>


# Let's see what happened if we provide the duplicate element to the set.
set1= {1,2,3,4,4,5,6,7}
print(f"Return set with unique elements : {set1}")          # Output=> Return set with unique elements : {1, 2, 3, 4, 5, 6, 7}