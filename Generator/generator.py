
# generators
# generators are iterators...

# iterator , iterable

l=[1,2,3,4]     # iterable
#for i in l:
   # print(i)

#i=iter(l)
#print(next(i))
#print(next(i))
#print(next(i))
#print(next(i))


for num in map(lambda a : a**2 , l):        # iterator
    print(num)



# l=[1,4,5,6,9]        
# memory...[......................] list
# memory......(1)   generator

#NOTE :- when we use our sequence(list) many time then we use list..otherwish we use 
        #   generator