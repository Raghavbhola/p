# Decorators:-decorators are a way to enhance functions or methods without changing their actual code.
#  Eg:-> use @ to know i.e. Decorator.
#(1)---------------------->
'''def change_case(arg):
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

@change_Uppercase
def my_uppercase():
    return"hello KaRAn, how Are yOu?"

@change_lowercase
def my_lowername():
    return"hello KaRAn, how Are yOu?"

@change_Uppercase
def my_uppercase1():
    return"Where there is a will there is a way.this is Karan speaking wHo Loves to Code"

print(my_lowername())
print(my_uppercase())
print(my_uppercase1())'''
#(2)------------------------------------->
def greet_decorator(arg):
    def inner_fun1():
        #print("Hello" ,arg())
        return "Hello! " + arg() + " Have a nice day."
    return inner_fun1  

def change_uppercase(arg):
    def inner_func2():
        return arg().upper()
    return inner_func2
    
@greet_decorator    
@change_uppercase
def my_greeting():
    return"We are Indian, Shubham Tiwari here,"



@greet_decorator
def your_greeting():
    return"We are Indian, Shubham Tiwari here,"

print(my_greeting())       #Hello! WE ARE INDIAN, SHUBHAM TIWARI HERE, Have a nice day.
print(your_greeting())     #Hello! We are Indian, Shubham Tiwari Here, Have a nice day.
