
# List vs generator..
# TIME CHECK ...

import time

#t1=time.time()
#l=[i**2 for i in range(10000000)] # 10 Milion 
#print(time.time() - t1)

t3=time.time()
g=(i**2 for i in range(10000000)) # 10 Milion
print(time.time() - t3)

# WHEN WE USE LIST AND WHEN WE USE GENERATOR...
# = We will use list when we use sequence many time and  we will use generator when 
#   we use sequence one time..
