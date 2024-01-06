def add(x):          # here, we are creating a function add and passing the parameter  
    return x+1      
def sub(x):          # here, we are creating a function sub and passing the parameter  
    return x-1   
def operator(func, x):    # here, we are creating a function and passing the parameter  
    temp = func(x)    
    return temp    
print(operator(sub,10))  # here, we are printing the operation subtraction with 10  
print(operator(add,20))   # here, we are printing the operation addition with 2