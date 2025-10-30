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


