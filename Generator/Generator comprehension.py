
# List comprehension..
square=[i**2 for i in range(1,11)]
print(square)


# Genertor comprehension..

# NOTE:- we use parenthesis() instead of [] in generator comprehension...

square2=(i**2 for i in range(1,11))

for num in square2:
    print(num)

# also we can use 
print(list(square2))