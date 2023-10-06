# OLD METHOD....

def func(s):
    if len(s) > 5:
        return True
    else:
        return False
name="Abhijit"
print(func(name))


# Using lambda...
str_len=lambda s : True if len(s)>5 else False
print(str_len('knowledge'))

print(str_len('skill'))