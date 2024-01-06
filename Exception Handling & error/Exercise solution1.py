# make a function 'devide'
# divide(a,b)
#print(divide(4,2)) # 2
# print(devide(4,0)) # plz dont devide by zero ,
# print(devide('4' , 2)) # plz input nubers only

def devide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print("You can't devide any number by zero..")
    except TypeError:
        print("Plz enter the intiger...")
    except:
        print("unexpected error..")


print(devide(10,0))         # Output=> You can't devide any number by zero..

print(devide(5,"6"))         # Output=>Plz enter the intiger...

