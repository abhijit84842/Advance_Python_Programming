# Decorator exercise..

# calculate the time to run the code...

import time

t1=time.time()

print("this is line 1..")

x=5
if x==5:
    print("x is equal to 5")
    print("this is line 2..")

t2=time.time()

total_time=t1-t2
print(total_time)

