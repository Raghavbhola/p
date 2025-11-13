#Python Modules:-A file containing python code, Eg.-Function and variable, that can be ignored and used in other python program.
#(1)----------------------------->
#import math
#print(math.sqrt(16))
#print(math.pi)
#print(math.sqrt(25))
#(2)----------------------------------**Print krvane ke liye alag se new file bananni hoegi:-mymodule.py--------------------- 
import mymodule
 
print(mymodule.print_message(" Alice "))       #Hello, Alice welcome to my module
print(mymodule.print_message(" Bob "))         #Hello, Bob welcome to my module
print(mymodule.print_message(" Microsoft "))   #Hello, Microsoft welcome to my module
print("Hello Buddy,How are you!")              #Hello Buddy,How are you!
#(3)------------------------------------------->
from importlib import reload
import mymodule
reload(mymodule)

print(mymodule.print_message(" Alice "))                       #Hello, Alice welcome to my module
print(mymodule.print_message(" MY Baby!how are you  & "))      #Hello, Hello! MY Baby!how are you  &  welcome to my module
print(mymodule.print_message(" Hello! Karan Aujla "))          #Hello, Hello! Karan Aujla welcome to my module

from importlib import reload
import mymodule

print(mymodule.print_message(" Karan Aujla "))
print(mymodule.Sum_numbers(5,10))             #15
print(mymodule.multiply_numbers(5,10))        #50
print(mymodule.subtract_numbers(10,2))        #8
print(mymodule.power_numbers(5,2))            #25
print(mymodule.divide_numbers(10,2))          #5.0
print(mymodule.multiply_numbers(7000000,90000))     #630000000000
print(mymodule.power_numbers(9000,10))              #3486784401000000000000000000000000000000
#--------------------------------------------------------------------------------------------------------------
#**NOTE-[*] use krne se Sab kuch select krdega.
#ALIAS- You are referring to the same thing.
#*Directory means:-[Folder] **dir:-If particular module, Which functions exist in it?
#(4)--------------------------------------------------------------------------------->
import mymodule as mm   #import with alias  *Nick name of mymodule:->mm

print(mm.print_message(" Karan Aujla "))     #Hello, Karan Aujla welcome to my module
print(mm.Sum_numbers(99,5))                  #104
print(mm.multiply_numbers(88,67))            #5896
print(mm.subtract_numbers(87,98))            #-11
print(mm.power_numbers(8,7))                 #2097152
print(mm.divide_numbers(90,7))               #12.857142857142858

print(dir(mm))           #**It only prints the alphabet.
#(5)------------>
import math 
print(dir(math))

import matplotlib
print(dir(matplotlib))

#Predefined/Build-in modules:->like modules already defined on Python path.
#(1)------------->
a=[12,21,43,224,5,73,76,67,775,336,77,1224]

print(max(a))   #1224
print(min(a))   #5
print(sum(a))   #2933
  
import random
print(dir(random))
print(random.randiant(1,100))   

#randiant:->Where to start and where to end, and it only prints integer values.
#Random:->only have print 16 or 17 digit, This can start from a point and anyone can generate it, and it generates uniquely.
#(1)--------------------->
import random
print(dir(random))
random.randint(1,10000)
print(random.random())
#(2)--------------------->
import math
print(math.sqrt(16))   #4.0
print(math.pi)         #3.141592653589793
#print(math)