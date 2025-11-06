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

from importlib import reload
import mymodule
reload(mymodule)

print(mymodule.print_message(" Alice "))                       #Hello, Alice welcome to my module
print(mymodule.print_message(" MY Baby!how are you  & "))      #Hello, Hello! MY Baby!how are you  &  welcome to my module
print(mymodule.print_message(" Hello! Karan Aujla "))          #Hello, Hello! Karan Aujla welcome to my module