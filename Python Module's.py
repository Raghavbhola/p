#Python Modules:-A file containing python code, Eg.-Function and variable, that can be ignored and used in other python program.
#(1)----------------------------->
#import math
#print(math.sqrt(16))
#print(math.pi)
#print(math.sqrt(25))
#(2)----------------------------------**Print krvane ke liye alag se new file bananni hoegi:-mymodule.py--------------------- 
'''import mymodule
 
print(mymodule.print_message(" Alice "))       #Hello, Alice welcome to my module
print(mymodule.print_message(" Bob "))         #Hello, Bob welcome to my module
print(mymodule.print_message(" Microsoft "))   #Hello, Microsoft welcome to my module
print("Hello Buddy,How are you!") '''             #Hello Buddy,How are you!
#(3)------------------------------------------->
'''from importlib import reload
import mymodule
reload(mymodule)

print(mymodule.print_message(" Alice "))                       #Hello, Alice welcome to my module
print(mymodule.print_message(" MY Baby!how are you  & "))      #Hello, Hello! MY Baby!how are you  &  welcome to my module
print(mymodule.print_message(" Hello! Karan Aujla ")) '''         #Hello, Hello! Karan Aujla welcome to my module

'''from importlib import reload
import mymodule

print(mymodule.print_message(" Karan Aujla "))
print(mymodule.Sum_numbers(5,10))             #15
print(mymodule.multiply_numbers(5,10))        #50
print(mymodule.subtract_numbers(10,2))        #8
print(mymodule.power_numbers(5,2))            #25
print(mymodule.divide_numbers(10,2))          #5.0
print(mymodule.multiply_numbers(7000000,90000))     #630000000000
print(mymodule.power_numbers(9000,10))   '''           #3486784401000000000000000000000000000000
#--------------------------------------------------------------------------------------------------------------
#**NOTE-[*] use krne se Sab kuch select krdega.
#ALIAS- You are referring to the same thing.
#*Directory means:-[Folder] **dir:-If particular module, Which functions exist in it?
#(4)--------------------------------------------------------------------------------->
import mymodule as mm   #import with alias

print(mm.print_message(" Karan Aujla "))     #Hello, Karan Aujla welcome to my module
print(mm.Sum_numbers(99,5))                  #104
print(mm.multiply_numbers(88,67))            #5896
print(mm.subtract_numbers(87,98))            #-11
print(mm.power_numbers(8,7))                 #2097152
print(mm.divide_numbers(90,7))               #12.857142857142858

print(dir(mm))