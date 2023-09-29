laptop_specification={
    'name' : "Hp",
    'processor' : 'intel i5 5th gen',
    'storage' : 'SSD 256 + 1 TB Hard disk',
    'os' : 'Windows 10 pro',
    'Display' : "14 inch"


}
# add data in dictionaries...
laptop_specification['ram']=8
print(laptop_specification)



# POP method...
deleted_items=laptop_specification.pop('os')
print(deleted_items)
print(laptop_specification)

