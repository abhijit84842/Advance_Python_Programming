 # Dictonaries introduction 

'''
1) What are dictionaries?
=Dictionaries are used to store data values in key:value pairs.

    A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

    As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

    Dictionaries are written with curly brackets, and have keys and values:


2) Which type of data dictionaries store?
=Dictinaries store anything like numbers , string , list ,dictionary.
'''
# why we use dictionaries?
# = Because of limitation of lists , list are not enough to represent real data.



 # How to create dictionaries?
user_info={
  'name' : 'abhijit',
  'age'  : 23,
  'fav_food' : ['chicken' , 'banana' , 'rice'],
  'fav_movie' : ['Money heist' , 'Master']
 }
print(user_info)

print(user_info['fav_movie'])
print(user_info['fav_movie'])


# Add data to empty dictionarie..
user_info1={}
user_info1['name']='Soumi Sen'
user_info1['age']=25
print(user_info1)







