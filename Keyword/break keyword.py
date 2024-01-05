'''The break is a keyword in python which is used to bring the program control out of the loop. The break statement breaks the loops one by one, i.e., in the case of nested loops, it breaks the inner loop first and then proceeds to outer loops. In other words, we can say that break is used to abort the current execution of the program and the control goes to the next line after the loop.'''



my_list=list(range(1,21))
for item in my_list:
    # if item matched
    if item==11:        # because loop searching by indexing
        print("Successfully Matched Item")
        break
    print(item)
#print(my_list)

'''
Output=> 1
2
3
4
5
6
7
8
9
10
Successfully Matched Item
'''