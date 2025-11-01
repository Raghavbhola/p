#Function's=> A block of code that performs a specific task, can be reused, takes input and returns output.
# def(keyword who tells compiler that we are defing a function). function_name(parameter/arguments):
#3Types of function:->
#(1)built-in function:-print(),input(),len(),type(),str(),float(),sum(),Min(),Max(),obs(),round()
#(2)User-defined function:-> functions defined by the user using def keyword.
#(3)Function syntax:->def function_name(parameters "self" must to be provided).
#(1)
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
#(2)
kids_name("Shivani","Rohan","Aarav","Kabir","Kiara")    #Function call with 5 argument
kids_name("kanish","kashish","rohan")                   #Function call with 3 argument
kids_name("A","B","c","d","e","f","g")                  #Function call without argument-will not give error because parameter is variable number of arguments.
#*NOTE-the term parameter and argument can be used from the same thing, information that are passed into a function.
#from a function prospective:->
#Parameter-is a function listed inside the parenthesis in the function definition.
#Argument-value that is sent to the function when it is called argument.

#KEYWORD ARGUMENT:-> Arguments that are passed to a function by explicity speciafying the parameter name.
#(1)
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

#(2)
def add():
    a=int(input("Enter first number:"))   #taking input from use.
    b=int(input("Enter second number"))   #taking input from use.
    print(a+b)    #return statement-returns the value to the caller

add()    #function call with argument
#(3)
def print_lastName(**p_info): #function with variable number of keyword arguments - **kwargs store all arguments in a dictionary
    print("Total last name of the person is :", p_info["lastName"]) #printing total number of arguments

print_lastName(lastName="Sharma", firstName="Yash", age=25, city="New Delhi", country="India", pinCode=110001) #function call with four keyword arguments
print_lastName(firstName="Raghav", age=30, city="Mumbai", lastName="India", pinCode=400001) #function call with three keyword arguments
print_lastName(lastName="Verma", firstName="Shubham") #function call with two keyword arguments
#print_lastName() #function call without argument - will not give error
#(4)
def kids_name(**kids):       #parameterized function with variable number of argument
    print("the youngest child is "+kids["youngest"])  #accessing last element
    #print("end of function")

kids_name(thirdyoungest="shivani",secondyoungest="rohan",youngest="arrav",fourthyoungest="kabir")  #function call with four parameter
kids_name(youngest="kanish",secondyoungest="rohan",thirdyoungest="kiara")   #function call with three parameter
kids_name(youngest="verma",secondyoungest="sharma")   #function call with second parameter
kids_name(fourthyoungest="A",secondyoungest="B",thirdyoungest="C",youngest="D",fifthyoungest="E",sixthyoungest="f")


#Return type:->return a value and exists the function.
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