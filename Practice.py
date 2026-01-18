#Min of 2 numbers:-
a=int(input("enter a number"))
b=int(input("enter a number"))

if a<b:
    print(a)
else:
    print(b)

#--------------------------------->
#is number odd or even:
n=int(input("enter a number"))

if n%2 == 0:
    print(f"This is even numbber:-")
else:
    print(f"This is an odd number:-0")    

#--------------------------
#sum of numbers from 1 to N:--->
N=int(input("enter a number"))
count=1
sum=0
while count<=N:
    sum=sum+count
    count=count+1

print(sum)

#---------------------------------------------
#to check it is prime number or not,if it is prime, check its a odd numberor a even number?
num =int(input("enter a number to check prime or not"))
for i in range (2,num):
   if (num%i)==0:
      print(f"{num}%{i}={num%i}")
      print(num,"is not a prime number")
      break
   else:
      print(num,"is a prime number")
   
#-----------------------------------------------   
#generate a array of elements of multiple of 10 till 1000 and then remove the elements from that array which is divisible by 3 and 5
import array as arr
arr =arr.array('i',[10,20,30,40,50,60,70,80,90,100])
for i in arr:
    if i % 3 or 5== 0:
        arr.remove(i)
print(arr)

#---------------------------------------------------
#declare a string of 15 words, then create a list in the manner that there shouldn't be any vowel
s=" eko rakhi jaat ne pyar rakhi phona cho baade ethe fiir de vepaar lage onaa choo"

for i in s:
    if i not in "aeiou":
        print(i,end="")

#---------------------------------------
#sum of numbers from 1 to N:->
N=int(input("enter a number"))
count=1
sum=0
while count<=N:
    sum=sum+count
    count=count+1

print(f"enter a number:-",(sum))    


#range -------------------------------------->
for i in range(108):  #start- by default 0,stop-n-1, step-by default 1
    print("Ram Ram",i+1)

#--------------------------------------------
#Write a Python program to find factorial of a number!?
num = int(input("Enter a number:"))
def factorial_recursive(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result    

print("factorial of", num ,"is:-", factorial_recursive(num))
    
#---------------
# Write a Python program to reverse a string without using built-in functions like? at least 4-5 character.


#Without using any string methods, try to print the following: 123....n
n = int(input())
    
for i in range(1,n+1):
        
    print(i,end="")

    