
# advance min() and max() ..
numbers=list(range(1,11))
print(max(numbers))
print(min(numbers))

# Advance way..
def func(item):
    return len(item)
names=['TCS','EY','CAPGIMINI','COGNIZANT']
print(min(names , key=func))





# find the score according to score..
student1={
    'abhijit' : {'score' : 90 , 'age' : 52},
    'Sikha' : {'score' : 80 , 'age' : 42},
    'samir' : {'score' : 25 , 'age' : 24}
}

print(max(student1 , key=lambda items : student1[items]['score']))