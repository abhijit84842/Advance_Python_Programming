def my_sum(*args):
    if all([(type(i) == int or type(i)==float) for i in args ]):

        total=0
        for num in args:
            total=total+num
        return total
    else:
        return "Worng input"
print(my_sum(1,2,3,4.5,63.4))       # Output :- 73.9

print(my_sum(1,2,3,4.5,63.4 , 'coding'))   #Output:-  Worng input