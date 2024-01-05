'''Set can be performed mathematical operation such as union, intersection, difference, and symmetric difference. Python provides the facility to carry out these operations with operators or methods'''

# Python also provides the union() method which can also be used to calculate the union of two sets.
Days1 = {"Monday","Tuesday","Wednesday","Thursday","Sunday" }    
Days2 = {"Friday","Saturday","Sunday"}   

print(Days1.union(Days2))

# Create three sets  
set1 = {1, 2, 3}  
set2 = {2, 3, 4}  
set3 = {3, 4, 5} 
print(set1.union(set2,set3))        # Output=> {1, 2, 3, 4, 5}