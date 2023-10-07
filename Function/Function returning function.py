
def outer_func(msg):
    def inner_func():
        print(f"The messeges is :- {msg}")
    return inner_func
var=outer_func("i am a coder")
var()