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