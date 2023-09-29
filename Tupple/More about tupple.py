# Looping in tuples..
# Tuple with one element..
# Tuple with out paranthisis..
# Tuple unpacking.
# List inside tuple..
# Some function that you can use tuple..



# Looping in tuples..

mixed=(1,"two", 3 , "four",5)
for i in mixed:
    print(i)




# tuple with one element..
num=(1,)
word=("abhi",)
print(type(num))
print(type(word))
# NOTE:-you need to use , in tuple..either it accept python as e inter value..



# tuple with out parenthesis..
name="abhijit" , "ram" , "shyam"
print(name)




# tuple unpacking...
name=("abhijit das","sikha das","samir das","subhajit das","raja das")
name1,name2,name3,name4,name5=(name)
print(name1)
print(name2)




# list in side tuple..
name=("abhijit","samir",["subhajit","sikha","raja"])

name[2].pop()          # we can pop list but not pop tuples
print(name)

name[2].append("Ani")
print(name)





# some function you can use with tuples..
# min(), max(),sum()

mixed=(1,2,3,4,5.6,7,8.9,9,10.2)
print(min(mixed))

print(max(mixed))

print(sum(mixed))