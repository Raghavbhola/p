#Lambda Function:->Small anonymous functions defined withe the lambda keyword. They can take any numbers of arguments but can only have one expression.

#(1)--------------------->
x=lambda a: a*1**5
print(x(5))       #5
print(x(50))      #50
print(x(500))     #500
print(x(5000))    #5000

x=lambda a: a*9**5
print(x(50))      #2952450
print(x(500))     #29524500
print(x(5))       #295245
print(x(90))      #5314410
#(2)---------------------------->
y=lambda a,b: a*b
print(y(500,100))      #50000
print(y(999,888))      #887112
print(y(5000,78978))   #394890000
print(y(600,6666))     #3999600
#(3)---------------------------->
w=lambda a,b,c: a+b+c
print(w(500,100,200))      #800
print(w(999,999,99))       #2097
print(w(66600,8880,3330))  #78810

# Use of Lambda function:->The power of lambda function is good when you them as an anonymous function inside another function.
#(1)------------------------------->
def sum_function(n):
    return lambda a: a*n

print(sum_function(10)(5))   #50
print(sum_function(10)(20))  #200
#(2)------------------------------->
def sum_function(n):
    return lambda a: a%n

print(sum_function(10)(5))   #50
print(sum_function(10)(20))  #200
#(3)------------------------------->
def sum_function(n):
    return lambda a: a*n

print(sum_function(10)(5))   #50
print(sum_function(10)(20))  #200

result=sum_function(10)
print(result(20))         #200
result=sum_function(200)
print(result(100))        #20000

#(4)-------------------------------->
def sum_function(n):
    return lambda a: a**n

print(sum_function(10)(5))   #9765625
print(sum_function(10)(20))  #10240000000000

result=sum_function(10)
print(result(20))         #10240000000000
result=sum_function(20)
print(result(100))        #10000000000000000000000000000000000000000
#(5)------------------------------->
def sum_function(n):
    return lambda a: a+n

print(sum_function(10)(5999))   #6009
print(sum_function(10)(29860))  #29870

result=sum_function(90)
print(result(205637287))         #205637377
result=sum_function(200100000000000000000)
print(result(187676987687367000)) #200287676987687367000
#(6)------------------------------->
def sum_function(n):
    return lambda a: a-n

print(sum_function(10)(5999))   #5989
print(sum_function(10)(29860))  #29850

result=sum_function(90)
print(result(205637287))         #205637197
result=sum_function(200100000000000000000)
print(result(187676987687367000)) #-199912323012312633000
#(7)------------------------------->
def sum_function(n):
    return lambda a: a/n

print(sum_function(10)(5999))   #599.9
print(sum_function(10)(29860))  #2986.0

result=sum_function(90)
print(result(205637287))         #2284858.7444444443
result=sum_function(200100000000000000000)
print(result(11234556))          #5.614470764617691e-14
#-------------------------------------------------------------------------------------------------------
# Lambda function are often used with built-in functions like filter(),Sorted() and reduce()

#Filter():- Functions creates a list of items for which the function returns true.
numbers=(5,10,15,20,25,30,35,40,45,50,55,60)
even_numbers=tuple(filter(lambda x:x%2==0,numbers))
print(even_numbers)      #(10, 20, 30, 40, 50, 60)

odd_numbers=tuple(filter(lambda x:x**2<1000,numbers))
print(odd_numbers)      #(5, 10, 15, 20, 25, 30)

#Map():->Functions applies a given function to all items in an input list
numbers=(5,10,15,20,25,30,35,40,45,50,55,60)
squared_numbers=tuple(map(lambda x:x**2,numbers))   #**Map
print(squared_numbers)  #(25, 100, 225, 400, 625, 900, 1225, 1600, 2025, 2500, 3025, 3600)

#Sorted():-> Function returns a sorted list of the specified iterable object.
#**When we sort then, we need to sorted as key. because key makes list
fruits=['banana','apple','cherry','kiwi','mango','orange','papaya']  
sorted_fruits=sorted(fruits,key=lambda x: len(x))  #sort by length
print(sorted_fruits)    #['kiwi', 'apple', 'mango', 'banana', 'cherry', 'orange', 'papaya']

fruits=['banana','apple','cherry','kiwi','mango','orange','papaya','blueberry','strawberry','fig'] 
sorted_fruits=sorted(fruits,key=lambda x: len(x))
print(sorted_fruits)    #['fig', 'kiwi', 'apple', 'mango', 'banana', 'cherry', 'orange', 'papaya', 'blueberry', 'strawberry']

#Generator:->Function that return an iterable set of items, one at a time, in a special way.
#            The generate values on the fly and do not store them in memory, making efficient for large datasets compared to lists.
#NOTE:-Generator are the functions that are pause and resume their execution.
#(1)--------------------------->
#li=[1,2,3,4,5,6,7]
#for value in li:
 #   print(value,end=",") #1,2,3,4,5,6,7

def my_func():
    print("start")
    return[1,2,3,4,5,6,7]

def my_generator():
    yield 1,13,14,15,16,
    yield 2
    yield 3
    yield 4
    yield 5

gen=my_generator()

#print(value)              #7
print(type(my_generator))  #<class 'function'>
print(id(50))              #140708160043336
print(my_func)             #<function my_func at 0x0000024A30A71080>
#(2)--------------------------------->
def my_func():
    print("start")
    return[1,2,3,4,5,6,7]

def my_generator():
    yield 1,13,14,15,16,
    yield 2
    yield 3
    yield 4
    yield 5

gen=my_generator()

print(next(gen))  #(1, 13, 14, 15, 16)
print(next(gen))  #2
print(next(gen))  #3
print(next(gen))  #4
print(next(gen))  #5
#print(next(gen))   #This will raise stopiteration error

#gen=my_generator
#print(gen(3))    #This will give error

#NOTE-(1)yeild is keyword or it's a compulsary in generator, yield is normal function,unique and who defines generator. 
#    (2)Never yeild incounter the function,The value is run whenever, next time generator is called it continous from where it left off.
#       Never generator store a value. 
#** huge-range Generator:->
#(1)---------------->
def huge_range(n):
    for i in range(n):
        print(i)

print(huge_range(100))
#(2)---------------->
def huge_range(n):
    for i in range(n):
        yield i

gen=huge_range(100)

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
 
#for value in gen:
#    print(value) 
#--------------------
#def huge_range(n):
#    for i in range(n):
#        yield i

#print(i) 

#gen=huge_range(100)

#**Fabonacci series:-> Previous two numbers-->Sum
#(1)------------->
li=[]
def f_series(n):
    #li.append(n)
    if n<=1:
        return n
    else:
        return f_series(n-1) + f_series(n-2)

print(f_series(2))   
print(sum(li))
print(li)
#(2)----------------------->
def fibonacci_generator():
    a,b,=0,1
    while True:
        yield a 
        a,b=b,a+b

fib_gen=fibonacci_generator()
for _ in range (100):
    print(next(fib_gen))       
#(3)----------------------->
def fibonacci_generator():
    a,b,=0,1
    while True:
        yield a 
        a,b=b,a+b

fib_gen=fibonacci_generator()
for _ in range (120):
    print(next(fib_gen)) 

#Send():-It allows you to send data (a value) to the generators.
def echo_generator():
    while True:
        got_value=yield
        print  ("The value is:-", got_value)

gen=echo_generator()
next(gen)
gen.send("Raghav")
gen.send("Shubham")
gen.send("parth")    
gen.send("Akash") 
gen.send("Kunal")

#print(type(Shubham)) #This will give you name error.
#print(id(Shubham))

#Close:-This method is use to step the generator 
#(1)----------------->
def my_gen():
    try:
        yield 1
        yield 2
        yield 3
        yield 4
    finally:
        print("Generator closed")

gen=my_gen()
print(next(gen))
gen.close()
#NOTE:->Finally:-> m print hoga hi hoga ...or yeh try: or Catch: ke sath hi use hoga.
#(2)------------------------->
def my_gen():
    try:
        yield 1
        yield 2
        yield 3
        yield 4
    finally:
        print("Generator closed")

gen=my_gen()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
gen.close()
#print(next(gen))

#NOTE->*Stack-Last-in,First-out[LIFO]
#      *Queue-First-out,First-out[FIFO]
#      *Push-enter a person
# ---------------------------------------------LIST------------------------------------------------------
#ordered, changeable and allow duplicates, and items are indexed.
#(1)---------------->
li=["apple","banana","guava","peach","cherry","guava","peach"]      
S="this is a good boy"
li[0]="raghav"
print(li)    #['raghav', 'banana', 'guava', 'peach', 'cherry', 'guava', 'peach']
#(2)--------------->
li=["apple","banana","guava","peach","cherry","guava","peach","cherry"]
print(li[5])  #guava
print(li)     #['apple', 'banana', 'guava', 'peach', 'cherry', 'guava', 'peach', 'cherry']
#(3)--------------->
t1=list(('apple','guava','peach','cherry'))
print(t1)       #['apple', 'guava', 'peach', 'cherry']
print(S[-3])    #b
print(li[-3])   #guava
print(li[-5:])  #['peach', 'cherry', 'guava', 'peach', 'cherry']
#(4)----------------->
nam=["aakash","Karan","kunal","shubham"]
print(nam[-1])         #shubham
print(nam[-4:-1])      #['aakash', 'Karan', 'kunal']
print(nam[-3])         #Karan
print(nam[-5:-2])      #['aakash', 'Karan']
print(nam)             #['aakash', 'Karan', 'kunal', 'shubham', 'Rajat', 'Right']
print(len(nam))        #6
nam.insert(2,"Shubham")
print(nam)             #['aakash', 'Karan', 'Shubham', 'kunal', 'shubham', 'Rajat', 'Right']
nam.insert(6,"yes")
print(nam)             #['aakash', 'Karan', 'Shubham', 'kunal', 'shubham', 'Rajat', 'yes', 'Right']
#(5)----------------->
li=["apple","banana","guava","peach","cherry","guava","peach"]
li.remove("peach")
print("Remove the element sucessfully")
print(li)              #['apple', 'banana', 'guava', 'cherry', 'guava', 'peach']
#pop:->Remove an element
li.pop()
print(li)              #['apple', 'banana', 'guava', 'cherry', 'guava']
li.pop(3)
print(li)              #['apple', 'banana', 'guava', 'guava']

del li[0]
#li.clear()
print("Remove the element sucessfully")
print(li)              #['banana', 'guava', 'guava']
li.clear()
print(li)              #[]