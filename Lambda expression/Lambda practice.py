
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