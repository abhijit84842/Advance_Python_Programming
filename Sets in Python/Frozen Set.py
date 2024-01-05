# FrozenSets
# In Python, a frozen set is an immutable version of the built-in set data type. It is similar to a set, but its contents cannot be changed once a frozen set is created.
# Frozen set objects support many of the assets of the same operation, such as union, intersection, Difference, and symmetric Difference. They also support operations that do not modify the frozen set, such as len(), min(), max(), and in.

FrozenSet=frozenset([1,2,3,4,5])
print(type(FrozenSet))      # Output=> <class 'frozenset'>

for i in FrozenSet:
    print(i)


Dictionary = {"Name":"John", "Country":"USA", "ID":101}     
print(type(Dictionary))    # Output=> <class 'dict'>
Frozenset = frozenset(Dictionary); #Frozenset will contain the keys of the dictionary    
print(type(Frozenset))     # Output=> <class 'frozenset'>
