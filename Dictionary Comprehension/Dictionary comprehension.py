# print 1 to 10 numbers square by dictionary comprehension..
# example={1:1,2:4,3:9}

square={i : i**2 for i in range(1,11)}
for k,v in square.items():
    print(f'key is {k} and value is {v}')



#Count the charecter..
str1="Abhijit"
word_count={i : str1.count(i) for i in str1}
print(word_count)