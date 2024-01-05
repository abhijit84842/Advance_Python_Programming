# add()
months={"January","February", "March", "April", "May", "June"}

months.add("july")
print(months)      # Output=> "January","February", "March", "April", "May", "June"


# update()
months.update(["August","September","October"])
print(months)          #Output => {'February', 'June', 'January', 'March', 'September', 'May', 'july', 'October', 'August', 'April'}



# discard()
months.discard("May")
print(months)        #Output =>{'January', 'April', 'June', 'March', 'February'}


# remove()
months.remove("April")
print(months)       #Output => {'June', 'February', 'March', 'January'}



# pop()
# # We can also use the pop() method to remove the item. Generally, the pop() method will always remove the last item but the set is unordered, we can't determine which element will be popped from set.
months={"January","February", "March", "April", "May", "June"}
poped_item=months.pop()
print(poped_item)    #Output =>    February

poped_item=months.pop()
print(poped_item)  #Output => January
print(months) 



