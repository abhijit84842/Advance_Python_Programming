'''We use Loop control statements in such cases. The continue keyword is a loop control statement that allows us to change the loop's control. Both Python while and Python for loops can leverage the continue statements'''

list1=list(range(1,11))

for i in list1:
    if i ==8:
        print("skip")
        continue
    print(i)

'''
Output:-> 1
2
3
4
5
6
7
skip
9
10
'''