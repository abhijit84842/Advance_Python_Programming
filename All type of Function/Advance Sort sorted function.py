fruits1=['grapes' , 'mango' ,'apple']  # we can use sort function in list..
fruits1.sort()
print(fruits1)




# we can't use sort function in tuple so we will use sorted function...
fruits2=('grapes' , 'mango' ,'apple')
print(sorted(fruits2))




# we can't use sort function in set so we will use sorted function...
fruits3={'grapes' , 'mango' ,'apple'}
print(sorted(fruits3))



# use in dictionaries..

boys=[
    {'ram' : 'A+', 'age' : 24},
    {'sam' : 'O+' , 'age' : 21},
    {'abhi' : 'B+' , 'age' : 20}
]

print(sorted(boys , key=lambda d : d['age']))
