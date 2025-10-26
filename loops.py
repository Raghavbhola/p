#L00PS:->Loops are used to repeat instructions. *TWO types of loops:-> FOR and WHILE. 
#        (for,while,for else,nested loops,break,continue,pass)
#(1)For loop->string,list,tuple,set,dictionary
s=[15,26,32,44,58,43,78,90,11,23]
for i in range(len(s)):
    print(i,s[i],sep="->")

s="This is thirsty crow,looking for a drop of water and it is very hot day"
s1=10
for i in s1:    
    #print(i)
#for i in s1:
    print(i,end="")

s1=str(1001)
print(type[s1])    
print(s1[3])       #set
for i in s1:
    print(i,end=".")

s= "Beautiful is better than ugly, Explicit is better than implicit,Simple is better than completed,Flat is beeter than nested,sparse is better than dence,Readability counts"
for i in s:
    if i not in "aeiouAEIOU":  #if it returns true,it will print consonats
        print(i,end="")

sum_tuple=(5,26,32,44,58,43,78,90,11,23)   #tuple
total=0
for i in sum_tuple:                    #loop for tuple
    print(i,total,sep="->")
    total=total+i
    print(i,total,sep="->")

li=[5,26,32,44,58,43,78,90,11,23]   #List
for i in li:                        #loop for List
    if i%2==0:
        print(i,"is even")
    else:
        print(i,"is odd")        
#(1)
for i in range(10,20):        #Range
    print(i)

for i in range(30,40):        #Range
    print(i)  
#(2)
for i in range(0,2,-1):       #Range
    print("Hello")
    
print("program ends here") 
#(3)
for i in range(10):  #single argument-stop,start-0,step-1
      print(i)  
for i in range(1,10,2):
      print(i)    
for i in range(11,21,15):
      print(i)        

#(1)
numbers={10:"ten",20:"twenty",30:"thirty",40:"forty",50:"fifty"}   #Dictionary
for i in numbers:
    print(i,numbers[i],sep="->")
#(2)    
numbers={10:"ten",20:"twenty",30:"thirty",40:"forty",50:"fifty"}
a=(numbers.keys())          #list of keys
print(a)
#(3)
for i in numbers.items():    #list of key-value pairs
    print(i)      
#(4)
a=numbers.get(10)          #accessing value using keys
for i in numbers:
    print(i,numbers[i],sep="->")         
#For-else loop:->
num=input("enter a number to write table:")
for i in range(1,11):
    print(f"{num}*{i}={num*i}")
    print(f"{num*i}")
else:  
    print("table is completed here ")    
    print("Program ends here/End of for-else loop")
        
 #While Loop:->It is used to repeat a block of code as long as a condition is true permanently, the loop will run indefinitely.
#While expression:Loop condition-by default it is ture
#statement(s)-block of code.
#code to be executed.
#(1)
count=0
print(id(count))
while count<5:
    print("count is:",count)
    count+=1
    print("loop ended")
#(2)
while True:
    print("hello")
    count=1
    while count<=8:
     print("hello")
    count=count+1

    print(count)

#print numbers from 1 to 5
i=1
while i <=5:
    print(i)
    i +=1

print("Loop ended")      
