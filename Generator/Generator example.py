# Create your first generator with the generator function..
# Generator function

def nums(n):
    for i in range(1,n+1):
        yield i

ad=nums(10)
for numbers in ad:
    print(numbers)