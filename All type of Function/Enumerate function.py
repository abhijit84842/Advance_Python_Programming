# We use enumerate function with for loop to track position of our item initerable..

# how we can do this without enumerate function...
names=['abhijit' ,'subhajit' ,'sikha' ,'samir', 'raja']

'''
# Old method..
pos=0
for i in names:
    print(f"{pos}......>{i}")
    pos=pos+1

    
'''

# Using enumerate function..
for pos , i in enumerate(names):
    print(f"{pos}....>{i}")
