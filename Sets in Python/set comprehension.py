# SET COMPREHENSION...
# we use {} in set.
# set has no key values only values.
# set is unorderd collection.

s={i**2 for i in range(1,11)}
print(s)

names={'abhijit' , 'sikha' ,'samir'}
first={i[0] for i in names}
print(first)