# Decorators:-decorators are a way to enhance functions or methods without changing their actual code.
#  Eg:-> use @ to know i.e. Decorator.
#(1)---------------------->
def change_case(arg):
    def inner_func():
        return arg().upper()
    return inner_func

@change_case
def my_name():
    return"Hello Karan,how are you?"

print(my_name())           #HELLO KARAN,HOW ARE YOU?
#Multi-Decorator------------------------------------->
#(1)------------->
def change_Uppercase(arg):
    def inner_func():
        return arg().upper()
    return inner_func

def change_lowercase(arg):
    def inner_func():
        return arg().lower()
    return inner_func
