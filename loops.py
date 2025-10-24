#L00PS:->(for,while,for else,nested loops,break,continue,pass)
#(1)For loop->string,list,tuple,set,dictionary
s=[15,26,32,44,58,43,78,90,11,23]
for i in range(len(s)):
    print(i,s[i],sep="->")

s="This is thirsty crow,looking for a drop of water and it is very hot day"
#s1=10
#for i in s1:    
    #print(i)
for i in s:
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