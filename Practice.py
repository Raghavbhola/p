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

#sum of numbers from 1 to N:->
N=int(input("enter a number"))
count=1
sum=0
while count<=N:
    sum=sum+count
    count=count+1

print(sum)