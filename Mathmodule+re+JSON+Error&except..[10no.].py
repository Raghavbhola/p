#--------------------------------------------{Math Module}-------------------------------------------------------------------
#*inbuilt math module and extensive mathematical functions (Math module)

x=min(5,10,15,2,15,0,-5,3)
y=max(5,10,25,2,15,0,-5,)
print(x)          #-5
print(y)          #25

z=(23354,34324,34234555,3332535,-32234)
print(max(z))     #34234555
print(min(z))     #-32234

#abs:-absolute(give +ve no.) [Even if it is -ve, it will still give +ve.]
#pow:-Power
a=abs(-100.25) #abs() Function returns the absolute (+ve) value of the specified number.
print(a)

b= pow(4,3) #pow()function returns the value of x to the power of x,y
print(b)          #64
c=pow(5964900,6)
print(c)
#-------------------------
import math as m #Alias
d=m.sqrt(15)     #math.sqrt()function returns the square root of (_)
print(d)
e=m.sqrt(29)
print(e)
#NOTE:-(1)Ceil:-Whatever value is given, it will give the [Nearest upper value] digit. But it will give an integer.
#      (2)floor:-[give Lowest no.]
#      (3)Round:-independent function [give nearest value]
#*Comb:->(n)Integar
#       *tell the no. of ways
#       *Probability

import math as m #Alias
d=m.ceil(4.2)   #math.ceil()function rounds a number UP to the nearest integar
print(d)   #5

e=m.floor(44.7) #math.floor()Func. rounds a no. DOWN to the nearest integar
print(e)   #44

r=round(58.1)   #round()Func. rounds a no. to the nearest integar
print(r)   #58

f=m.factorial(5)#math.Factorial returns the factorial of a no.
print(f)   #120

p=m.pi          #math.pi function returns the value of pi
print(p)   #3.14....

a=m.tau         #math.tau function returns the value of tau(2*pi)
print(a)   #6.28....

b=m.nan         #math.nan func. returns a floating point "Not a Number"[nan]value
print(b)   #nan

c=m.inf         #math.inf func. returns a floating point [+ve] Infinity Value
print(c)   #inf
#Comb--->
C=m.comb(8,3) #math.Comb(n,k) Func. returns the number of ways to choose K items from n item.
print(C)   #56 
