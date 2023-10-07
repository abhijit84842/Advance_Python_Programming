# function returning function(clousers)..
# clousers(first class function)

def to_power(x):
    def number(n):
        return n**x
    return number

square=to_power(2)
print(square(8))    # Output :- 64

cube=to_power(3)
print(cube(5))          # Output : -125