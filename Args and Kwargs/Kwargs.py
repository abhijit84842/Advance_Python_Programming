# kwargs = keyword argument..
# **kwargs(double star operator..)
# type of kwargs(dict)

def func(**kwargs):
    for k,v in kwargs.items():
        print(f"{k} : {v}")

d={
    'name' : 'Abhijit',
    'last name' : 'Das',
    'Roll_no' : 27
}

func(**d)