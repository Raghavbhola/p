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
   