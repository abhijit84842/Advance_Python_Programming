# To discover what is common between two or more sets in Python, apply the intersection() function.
# The intersection of two sets can be performed by the and & operator or the intersection() function.


set1 = {"Monday","Tuesday", "Wednesday", "Thursday"}    
set2 = {"Monday","Tuesday","Sunday", "Friday"} 
print(set1.intersection(set2))      # Output=> {'Monday', 'Tuesday'}




# The intersection_update() method removes the items from the original set that are not present in both the sets (all the sets if more than one are specified).
a = {"Devansh", "bob", "castle"}    
b = {"castle", "dude", "emyway"}    
c = {"fuson", "gaurav", "castle"}    
    
a.intersection_update(b, c)    
    
print(a)     # Output=> {'castle'}




# The difference of two sets can be calculated by using the subtraction (-) operator or difference() method. 
Days1 = {"Monday",  "Tuesday", "Wednesday", "Thursday"}    
Days2 = {"Monday", "Tuesday", "Sunday"}
print(Days1.difference(Days2))      # {'Thursday', 'Wednesday'}




# Symmetric Difference of two sets
# In Python, the symmetric Difference between set1 and set2 is the set of elements present in one set or the other but not in both sets. In other words, the set of elements is in set1 or set2 but not in their intersection.
a1 = {1,2,3,4,5,6}  
b1 = {1,2,9,8,10}  
c1 = a1.symmetric_difference(b1)  
print(c1)      # {3, 4, 5, 6, 8, 9, 10}   
