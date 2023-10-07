# Create your first generator with the generator function..
# Generator function

def nums(n):
    for i in range(1,n+1):
        yield i                     # NOTE:- yield is a keyword so you dont have to write i
                                        # in parenthesis beacuse yield its not function
                                        # i mean you can also write 'yield i' instead of, 
                                        #  'yield(i)'
                                
ad=nums(10) 
ad=nums(10)
for numbers in ad:
    print(numbers)