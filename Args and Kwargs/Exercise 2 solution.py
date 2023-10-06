# define a function 
# return a list if we write reverse_str=True then the hole string will be reverse and must be take 1st index Capital
# else , only string will be capital .

def func(l,**kwargs):
    if kwargs.get('reverse_str')==True:
        return [i[::-1].title() for i in l]
    else:
        return [i.title() for i in l]
    
names=['samir' , 'abhijit' , 'raj']            

print(func(names))              # Output :- ['Samir', 'Abhijit', 'Raj'] 

print(func(names , reverse_str=True))           # Output :- ['Rimas', 'Tijihba', 'Jar']
