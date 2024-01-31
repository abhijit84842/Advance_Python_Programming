class First:
    def sum(self,a,b):
        c=a+b
        return c

class Second:
    def sub(self,x,y):
        z=x-y
        return z
    
class Third(First , Second):
    def multiply(self,a1,b1):
        c1=a1*b1
        return c1
    
t1= Third()
sum=t1.sum(5,4)
print(sum)

multi=t1.multiply(5,6)
print(multi)
        