# Built in errors..
# Exception , How to handel them..
# Raise your own errors ,debugging , etc 

# Syntax error:-
def func:
pass


# Indentation error :-
def func():
    print('hello')         NOTE:- Space related error is indentation error..
 print('hi')

# name error:- When use any variable or anythigs thats not define then occur name error..

print(name)               NOTE:-name is not define..

# type error..
print(5 * 'abhijit')       NOTE:- we cant use integer with string..


# index error..
l=[1,2,3]
print(l[4])                NOTE:-Occur index error..

# Value error:- When you write any data type correct but input value is wrong then occur value error..
string= 'abhijit'
print(int(s))

# Attribute error :-

l=[1,2,3]
l.push('12')

# Key error :-
d={'name' : 'abhijit'}
print(d['age'])


