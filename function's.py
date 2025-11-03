#Function's=> A block of code that performs a specific task, can be reused, takes input and returns output.
# def(keyword who tells compiler that we are defing a function). function_name(parameter/arguments):
#3Types of function:->
#(1)built-in function:-print(),input(),len(),type(),str(),float(),sum(),Min(),Max(),obs(),round()
#(2)User-defined function:-> functions defined by the user using def keyword.
#(3)Function syntax:->def function_name(parameters "self" must to be provided).
#(1)---------------------------------------------------------->
def greet():
    print("Hello,Good morning!")
    li=[1,2,3,4,5,6,7,8,9,10]
    for i in range(len(li)):
        print(f"{li[i]}  have a great day!")

def printNamefunction(name):    #function with parameter/parameterized function
    print(" Hello "+ name +", good morning!")

printNamefunction("yashika")    #function call with parameter
printNamefunction("shubham")    #function call with parameter
printNamefunction("kunal")      #function call with parameter
printNamefunction("sham")    #function call with parameter
printNamefunction("mohit")    #function call with parameter
printNamefunction("sneha")      #function call with parameter
#printNamefunction()                            #function call with parameter-will give you error because parameter is mandatory.  
#printNamefunction("shubham","good evening")    #function call with parameter-will give you error because parameter is mandatory.

def kids_name(*kids):   #prameterized function with variable number of arguments
    print("Total number of kids:",len(kids))  #printing total no. of arguments
    print("the youngest child is",kids[len(kids)-1])  #accessing last elements
    print("End of function")          #Printing all elements
#(2)--------------------------------------------------->
kids_name("Shivani","Rohan","Aarav","Kabir","Kiara")    #Function call with 5 argument
kids_name("kanish","kashish","rohan")                   #Function call with 3 argument
kids_name("A","B","c","d","e","f","g")                  #Function call without argument-will not give error because parameter is variable number of arguments.
#*NOTE-the term parameter and argument can be used from the same thing, information that are passed into a function.
#from a function prospective:->
#Parameter-is a function listed inside the parenthesis in the function definition.
#Argument-value that is sent to the function when it is called argument.
#-------------------------------------------------------------------------------------------------------
#KEYWORD ARGUMENT:-> Arguments that are passed to a function by explicity speciafying the parameter name.
#(1)-------------------------------->
def printInfo(name,age):
    print("Name:",name)
    print("Age:",age)

printInfo(age=25,name="kunal")
printInfo(name="Raghav",age=30)
printInfo("Shubham",28)
printInfo("Aman",32)
'''OUTPUT
Name: kunal
Age: 25
Name: Raghav
Age: 30
Name: Shubham
Age: 28
Name: Aman
Age: 32'''

#(2)--------------------------------------------------------------------->
def add():
    a=int(input("Enter first number:"))   #taking input from use.
    b=int(input("Enter second number"))   #taking input from use.
    print(a+b)    #return statement-returns the value to the caller

add()    #function call with argument
#(3)-------------------------------------------------------------------------->
def print_lastName(**p_info): #function with variable number of keyword arguments - **kwargs store all arguments in a dictionary
    print("Total last name of the person is :", p_info["lastName"]) #printing total number of arguments

print_lastName(lastName="Sharma", firstName="Yash", age=25, city="New Delhi", country="India", pinCode=110001) #function call with four keyword arguments
print_lastName(firstName="Raghav", age=30, city="Mumbai", lastName="India", pinCode=400001) #function call with three keyword arguments
print_lastName(lastName="Verma", firstName="Shubham") #function call with two keyword arguments
#print_lastName() #function call without argument - will not give error
#(4)----------------------------------------------------------------------------->
def kids_name(**kids):       #parameterized function with variable number of argument
    print("the youngest child is "+kids["youngest"])  #accessing last element
    #print("end of function")

kids_name(thirdyoungest="shivani",secondyoungest="rohan",youngest="arrav",fourthyoungest="kabir")  #function call with four parameter
kids_name(youngest="kanish",secondyoungest="rohan",thirdyoungest="kiara")   #function call with three parameter
kids_name(youngest="verma",secondyoungest="sharma")   #function call with second parameter
kids_name(fourthyoungest="A",secondyoungest="B",thirdyoungest="C",youngest="D",fifthyoungest="E",sixthyoungest="f")

#------------------------------------------------------------------------------------------------------------------------------------
#Return type:->return a value and exists the function.
#(1)---->
def add(a,b):
    return a+b
def sub(a,b):
    return a-b    
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def mod(a,b):
    return a%b
#add------------------------------------------>
a=int(input("enter first number:"))
b=int(input("enter second number"))
c=10
d=20
addtion=add(a,b)
addtion1=add(c,d)
addition2=add(100,200)

print("addition:",add(a,b))
print("addition1:",add(c,d))      #30
print("addtion3:",add(100,200))   #300
#MUL------------------------------------------->
a=int(input("enter first number:"))
b=int(input("enter second number"))
c=10
d=20
multiply=mul(a,b)
multiply1=mul(c,d)
multiply2=mul(100,200)

print("multiply:",mul(a,b))      
print("multiply1:",mul(c,d))       #200
print("multiply2:",mul(100,200))   #20000
#sub-------------------------------------------->
a=int(input("enter first number:"))
b=int(input("enter second number"))
c=10
d=20
subtraction=mul(a,b)
subtraction1=mul(c,d)
subtraction2=mul(100,200)

print("subtraction:",sub(a,b))      
print("subtraction1:",sub(c,d))       #-10
print("subtraction2:",sub(100,200))   #-100
#div-------------------------------------------->
a=int(input("enter first number:"))
b=int(input("enter second number"))
c=10
d=20
division=div(a,b)
division1=div(c,d)
division2=div(100,200)

print("division:",div(a,b))      
print("division1:",div(c,d))       #0.5
print("division2:",div(100,200))   #0.5
#module----------------------------------------->
a=int(input("enter first number:"))
b=int(input("enter second number"))
c=10
d=20
module=mod(a,b)
module1=mod(c,d)
module2=mod(100,200)

print("module:",mod(a,b))      
print("module:",mod(c,d))       #10
print("module2:",mod(100,200))   #100
#(2)
def add(x,y):
    pass
def sub(x,y):
    pass
def mul(x,y):
    pass
def div(x,y):
    pass

x=int(input("enter first number:"))
y=int(input("enter second number:"))
add(x,y)
sub(x,y)
mul(x,y)
div(x,y)
print("end of the person",x,y)
#(3)--------------------------------------------->
def my_function(x,y):
    print(x**3)

my_function(10,5)      #1000
my_function(x=1,y=5)   #1
my_function(89,9)      #704969
my_function(999,32)    #99702999
#(2)---------------------------------------------->
def my_function(*,x,y):  #keyword only parameter
    print(x**3)
    print(y**3)

my_function(x=10,y=5)   #1000 /125
my_function(y=3,x=4)    #64  /27
#my_function(10,5)     #Type error:-my_function() takes 0 positional arguments but 2 were given
#-----------------------------------------------------------------------------------------------------
#Recurrsion:-> When a Function calls itself reapeatedly.                **Coders avoid recurrsion.
#(1)
#(1)-------------------->
def show(n):
    if (n==0):
        return
    print(n)
    show(n-1)
    print("END")
    
show(3)
#show(5)    
#(2)---------------------------->
def recur_func(n):
    if n>0:
        result=n+recur_func(n-1)
        print(result)
    else:
        result=0
        print(result)
    return result 

#recur_func(5)
recur_func(3)
#recur_func(10)
#(3)--------------------------->
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        print(n)
        return n*factorial(n-1)
    
print(factorial(5))
print(factorial(4))    
print(factorial(25))
#print(factorial(1000))
#(3)--------------------------->
def main(food):
    for i in food:
        print(i*2)

#main(s)
#food (["apple","banana","cherry","orange","kiwi","Mango"])  
#main (["sandwich","burger","pizza","pasta","salad"])
#main (food)
food=["apple","banana","cherry","orange","kiwi","Mango"]
main(food)
food1=["carrot","patato","cabbage","onion","spinach"]
main(food1)
#-------------------------------------------------------------------------------------------
#Scope of variable:->Local, global and Non-local.
#Local variable:-defined inside a function and can be accessed that function.
#Global variable:-defined outside a function and can be accessed anywhere in the program.
x=int(input("enter a number:"))

def find_even_odd(num):
    print(f"The number {num} is being checked")
    if num%2==0:
        return"even"
    else:
        return"odd"
    
result=find_even_odd(x)
print(f"The number{x} is {result}")
    