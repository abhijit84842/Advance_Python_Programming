
# OLD METHOD TO DEFINE A FUNCTION..

def func(num):
    if num%2==0:
        return True
    else:
        return False
print(func(7))

# Using lambda
is_even= lambda num : True if num%2==0 else False
print(is_even(8))       # Output : - True


# Define a function and print last char of a string..
last_char=lambda s : s[-1]
print(last_char('abhijit'))     # Output : - t


# TAKE A LIST AS A ARGUMENT..
# Example list
my_numbers = list(range(1,11))
# Example lambda function that takes a list and returns the sum of its elements
sum_list = lambda my_list: sum(my_list)

print(sum_list(my_numbers))