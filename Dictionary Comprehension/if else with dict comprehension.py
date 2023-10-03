# show the even and odd number by dictionary comprehension..
# Exapmle : - d={1:'odd' , 2 : 'even'}

even_odd={i : ('even' if i%2==0 else 'odd') for i in range(1,11)}
print(even_odd)