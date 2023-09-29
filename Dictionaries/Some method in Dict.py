# Formkey method...
# when we want to keep dictionary key's values default.. then we use formkey.

d1={
    'name' : 'abhijit',
    'address' : 'c.k town',
    'fav_movie' : ['coco','mater', 'pushpa']
}

d=dict.fromkeys(['name' , 'address'],'unknown')
print(d)



# get()
print(d1.get('address'))

if d1.get('fav_movie'):
    print("present")
else:
    print("Not present")



# copy method..
copy_dic2=d1.copy()
print(copy_dic2)





#clear()
d1.clear()       # it clear the full dictionaries..
print(d1)
