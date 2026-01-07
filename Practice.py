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

