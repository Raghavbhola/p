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